class Product: 
    def __init__(self, pid, name, price, stock): 
        self.pid = pid 
        self.name = name 
        self.price = price 
        self.__stock = stock   # private (Encapsulation) 
 
    def get_stock(self): 
        return self.__stock 
 
    def reduce_stock(self, qty): 
        if qty <= self.__stock: 
            self.__stock -= qty 
            return True 
        return False 
 
    def display(self): 
        print(f"{self.pid} | {self.name} | ₹{self.price} | Stock: {self.__stock}") 
 
 
class ECommerceSystem: 
    def __init__(self): 
        self.products = [] 
        self.cart = []   # stores (product, qty) 
 
    def add_product(self, product): 
        self.products.append(product) 
 
    def view_products(self): 
        print("\n--- Available Products ---") 
        for p in self.products: 
            p.display() 
 
    def add_to_cart(self, pid, qty): 
        for p in self.products: 
            if p.pid == pid: 
                if p.reduce_stock(qty): 
                    self.cart.append((p, qty)) 
                    print(f"Added to cart: {p.name} x {qty}") 
                else: 
                    print("Not enough stock!") 
                return 
        print("Product not found!") 
 
    def view_cart(self): 
        print("\n--- Cart Items ---") 
        if len(self.cart) == 0: 
            print("Cart is empty!") 
            return 
 
        total = 0 
        for item, qty in self.cart: 
            cost = item.price * qty 
            total += cost 
            print(f"{item.name} x {qty} = ₹{cost}") 
 
        print("Total Amount = ₹", total) 
 
    def apply_discount(self): 
        total = sum(item.price * qty for item, qty in self.cart) 
 
        if total >= 5000: 
            discount = 0.20 
        elif total >= 2000: 
            discount = 0.10 
        else: 
            discount = 0.0 
 
        final_amount = total - (total * discount) 
 
        print("\n--- Discount Bill ---") 
        print("Total Amount    :", total) 
        print("Discount Applied:", int(discount * 100), "%") 
        print("Final Amount    :", final_amount) 
 
 
# ------------------------- 
# Testing 
# ------------------------- 
 
system = ECommerceSystem() 
 
p1 = Product(1, "Laptop", 50000, 5) 
p2 = Product(2, "Mouse", 500, 20) 
p3 = Product(3, "Keyboard", 1500, 10) 
 
system.add_product(p1) 
system.add_product(p2) 
system.add_product(p3) 
 
system.view_products() 
 
system.add_to_cart(2, 2) 
system.add_to_cart(3, 1) 
system.add_to_cart(1, 1) 
 
system.view_cart() 
system.apply_discount() 
 
system.view_products() 
class Product: 
    def __init__(self, pid, name, price): 
        self.pid = pid 
        self.name = name 
        self.price = price 
 
    def display(self): 
        print(f"{self.pid} | {self.name} | ₹{self.price}") 
 
 
class Electronics(Product): 
    def __init__(self, pid, name, price, warranty_years): 
        super().__init__(pid, name, price) 
        self.warranty_years = warranty_years 
 
    def display(self): 
        print(f"{self.pid} | {self.name} | ₹{self.price} | Warranty: {self.warranty_years} yrs") 
 
 
class Clothing(Product): 
    def __init__(self, pid, name, price, size): 
        super().__init__(pid, name, price) 
        self.size = size 
 
    def display(self): 
        print(f"{self.pid} | {self.name} | ₹{self.price} | Size: {self.size}") 
 
 
class Cart: 
    def __init__(self): 
        self.items = []  # stores (product, qty) 
 
    def add_to_cart(self, product, qty): 
        self.items.append((product, qty)) 
        print(f"Added: {product.name} x {qty}") 
 
    def show_cart(self): 
        print("\n--- CART ITEMS ---") 
        if len(self.items) == 0: 
            print("Cart is empty!") 
            return 
 
        for product, qty in self.items: 
            print(f"{product.name} x {qty} = ₹{product.price * qty}") 
 
    def get_total(self): 
        total = 0 
        for product, qty in self.items: 
            total += product.price * qty 
        return total 
 
 
# Payment System (Polymorphism) 
class Payment: 
    def pay(self, amount): 
        print("Processing payment...") 
 
 
class CashPayment(Payment): 
    def pay(self, amount): 
        print(f"Cash Payment Successful: ₹{amount}") 
 
 
class UPIPayment(Payment): 
    def pay(self, amount): 
        print(f"UPI Payment Successful: ₹{amount}") 
class CardPayment(Payment): 
    def pay(self, amount): 
        print(f"Card Payment Successful: ₹{amount}") 
# Bill Generation 
def generate_bill(cart): 
    print("\n========== BILL ==========") 
    if len(cart.items) == 0: 
        print("No items in cart!") 
    return 
    total = 0 
    for product, qty in cart.items: 
        cost = product.price * qty 
        total += cost 
        print(f"{product.name} x {qty} = ₹{cost}") 
    
    print("--------------------------") 
    print("Total Amount = ₹", total) 
    # Discount Logic 
    if total >= 5000: 
        discount = 0.20 
    elif total >= 2000: 
        discount = 0.10 
    else: 
        discount = 0.0 

    final_amount = total - (total * discount) 
    print("Discount =", int(discount * 100), "%") 
    print("Final Amount = ₹", final_amount) 
    print("==========================") 
    
    return final_amount 
# ----------------------------------------- 
# Testing the System 
# ----------------------------------------- 
# Products 
p1 = Electronics(1, "Laptop", 50000, 2) 
p2 = Electronics(2, "Headphones", 2000, 1) 
p3 = Clothing(3, "T-Shirt", 800, "L") 
p4 = Clothing(4, "Jeans", 1500, "32") 
# Show products 
print("\n--- AVAILABLE PRODUCTS ---") 
p1.display() 
p2.display() 
p3.display() 
p4.display() 
# Cart 
cart = Cart() 
cart.add_to_cart(p2, 1) 
cart.add_to_cart(p3, 2) 
cart.add_to_cart(p4, 1) 
cart.show_cart() 
# Bill 
final_amount = generate_bill(cart) 
# Payment 
print("\n--- SELECT PAYMENT METHOD ---") 
print("1. Cash") 
print("2. UPI") 
print("3. Card") 
choice = int(input("Enter choice: ")) 
if choice == 1: 
    payment = CashPayment() 
elif choice == 2: 
    payment = UPIPayment() 
elif choice == 3: 
    payment = CardPayment() 
else: 
    print("Invalid payment option!") 
    payment = None 
if payment: 
    payment.pay(final_amount) 
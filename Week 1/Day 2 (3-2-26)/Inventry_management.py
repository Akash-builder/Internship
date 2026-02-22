inventory = {}  #inventory is dictionary

n = int(input("Enter number of products: "))

for i in range(n):
    product = input(f"Enter product name {i+1}: ")
    stock = int(input(f"Enter stock for {product}: "))
    inventory[product] = stock

print("\nAvailable Products:")

for product, stock in inventory.items():
    if stock > 0:
        print(product, "- Stock:", stock)

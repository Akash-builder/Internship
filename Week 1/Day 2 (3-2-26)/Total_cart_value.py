cart = [] #cart is list
total = 0

n = int(input("Enter number of items in cart: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    cart.append(price)

for price in cart:
    total += price

print("\nTotal Cart Value:", total)

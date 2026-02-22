cart = {}

cart["cart_value"] = float(input("Enter cart value: ₹"))
cart["membership"] = input("Enter membership (gold/silver/regular): ").lower()

membership_discount = {
    "gold": 5,
    "silver": 3,
    "regular": 0
}

if cart["cart_value"] >= 10000:
    base = 30
elif cart["cart_value"] >= 5000:
    base = 20
elif cart["cart_value"] >= 1000:
    base = 10
else:
    base = 0

extra = membership_discount.get(cart["membership"], 0)

total = base + extra
discount = cart["cart_value"] * total / 100
final = cart["cart_value"] - discount

print("\n----- BILL SUMMARY -----")
print("Cart Value      :", cart["cart_value"])
print("Membership      :", cart["membership"].title())
print("Discount %      :", total)
print("Discount Amount :", discount)
print("Final Amount    :", final)

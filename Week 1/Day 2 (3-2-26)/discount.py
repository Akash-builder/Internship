cart_value=float(input("Enter the total cart amount: "))

if cart_value>=10000:
    discount_percentage=30
elif cart_value>=5000:
    discount_percentage=20
elif cart_value>=1000:
    discount_percentage=10

discount=cart_value * (discount_percentage / 100)
final_value= cart_value - discount

print("The total amount is ",final_value)

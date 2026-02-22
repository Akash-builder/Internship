def even_odd(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("Enter the number : "))

print("Number is",even_odd(num))
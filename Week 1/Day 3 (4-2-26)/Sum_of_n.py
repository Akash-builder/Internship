def sum(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
num=int(input("Enter the number : "))
print("Sum of the numbers :",sum(num))
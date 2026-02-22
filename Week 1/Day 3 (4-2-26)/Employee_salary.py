def calculate_net_salary(basic_salary):
    hra = basic_salary * 0.20
    pf = basic_salary * 0.12

    net_salary = basic_salary + hra - pf
    return net_salary


basic = float(input("Enter the basic salary : "))
net = calculate_net_salary(basic)

print("Basic Salary:", basic)
print("Net Salary:", net)

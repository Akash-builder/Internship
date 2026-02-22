def max_num(num):
    maximum=num[0]
    for i in num:
        if i>maximum:
            maximum=i
    return maximum

list=[12,34,56,76,63,74,91,103,98,43,94,]
print("Maximum in the list :",max_num(list))
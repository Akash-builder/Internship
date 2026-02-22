percentages = [35, 67, 80, 29, 45]

results = list(map(lambda p: "Pass" if p >= 40 else "Fail", percentages))
print(results)

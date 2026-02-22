marks = []
total = 0

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

for m in marks:
    total += m

average = total / n

print("\nTotal Marks:", total)
print("Average Marks:", average)

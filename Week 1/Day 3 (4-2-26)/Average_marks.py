def calculate_grade(marks):
    total = 0

    # Add all marks
    for mark in marks:
        total += mark

    # Calculate average
    average = total / len(marks)

    # Decide grade
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


# Example input
marks_list = [75, 82, 68, 90, 77]

# Function call
grade = calculate_grade(marks_list)

print("Marks:", marks_list)
print("Grade:", grade)

def calculate_average_marks(filename): 
    try: 
        with open(filename, "r") as file: 
            marks = [] 
            for line in file: 
                line = line.strip() 
                try: 
                    marks.append(int(line)) 
                except ValueError: 
                    print(f"Invalid mark found: {line} (Skipped)") 
            if len(marks) == 0: 
                return "No valid marks found!" 
            average = sum(marks) / len(marks) 
            return average 
    except FileNotFoundError: 
        return "Error: File not found!" 
    except Exception as e: 
        return f"Unexpected Error: {e}" 
result = calculate_average_marks("marks.txt") 
print("Average Marks:", result) 
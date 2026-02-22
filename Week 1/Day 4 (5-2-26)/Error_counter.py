error_lines = [] 
error_count = 0 
with open("log.txt", "r") as file: 
    for line in file: 
        if "ERROR" in line: 
            error_count += 1 
            error_lines.append(line) 
with open("errors.txt", "w") as file: 
    file.writelines(error_lines) 

print("Total Errors Found:", error_count) 
print("Error lines saved in errors.txt")
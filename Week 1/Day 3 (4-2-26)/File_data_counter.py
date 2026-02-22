def file_data_counter(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename, "r") as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return line_count, word_count, char_count

file_name = "sample.txt"

lines, words, characters = file_data_counter(file_name)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)

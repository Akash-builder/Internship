def count_frequency(elements):
    frequency = {}

    for item in elements:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


data = [1, 2, 2, 3, 1, 4, 2, 3]

result = count_frequency(data)

print(result)

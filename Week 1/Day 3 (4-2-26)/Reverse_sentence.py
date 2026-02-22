def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    result = " ".join(reversed_words)
    return result

sentence = input("Enter the sentence : ")
output = reverse_each_word(sentence)

print(output)

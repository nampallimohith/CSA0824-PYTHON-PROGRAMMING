def reverse_word(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Example
input_word = input("Enter a word: ")
result = reverse_word(input_word)
print("Reversed word:", result)

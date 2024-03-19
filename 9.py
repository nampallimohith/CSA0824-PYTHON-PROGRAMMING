def modify_string(s):
    frequency = {}
    
    # Count the frequency of each character
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Replace characters based on their frequency and circular distance
    modified_string = ""
    for char in s:
        distance = frequency[char]
        new_char = chr((ord(char) - ord('a') + distance) % 26 + ord('a'))
        modified_string += new_char

    return modified_string

# Test Case
input_string = "elephant"
result = modify_string(input_string)
print(result)

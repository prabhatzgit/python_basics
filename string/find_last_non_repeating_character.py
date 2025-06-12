def find_first_non_repeating_character(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    for i in reversed(range(len(input_string))):
        if char_counts[input_string[i]] == 1:
            return input_string[i]
    return None

input_string = "abacabad"
last_non_repeating = find_first_non_repeating_character(input_string)

print(f"The last non-repeating character in '{input_string}' is: {last_non_repeating}")

input_string = "aabbcc"
last_non_repeating = find_first_non_repeating_character(input_string)
print(f"The last non-repeating character in '{input_string}' is: {last_non_repeating}")
def find_first_non_repeating_character(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in input_string:
        if char_counts[char] == 1:
            return char
    return None

input_str = "abacabad"
first_non_repeating = find_first_non_repeating_character(input_str)
print(f"The first non-repeating character in '{input_str}' is: {first_non_repeating}")
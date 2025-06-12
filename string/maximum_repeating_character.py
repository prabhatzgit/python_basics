def find_max_repeating_char_per_index(input_string):
    """
    Finds the character with the maximum frequency for every prefix of the
    given input string.

    For each index `i`, it considers the substring from the beginning up to
    and including `input_string[i]`, then identifies the character that
    appears most frequently within that prefix. If there's a tie in frequency,
    it returns the character that appeared first alphabetically among the
    most frequent ones.

    This version achieves the goal without using collections.Counter.

    Args:
        input_string (str): The string to analyze.

    Returns:
        list: A list of tuples. Each tuple contains (index, character, count),
              representing the maximum repeating character and its count
              for the prefix ending at that index.
    """
    results = []
    # Use a standard dictionary to keep track of character frequencies for the current prefix
    current_char_counts = {}

    for i, char in enumerate(input_string):
        # Update the count for the current character in the dictionary
        current_char_counts[char] = current_char_counts.get(char, 0) + 1

        if not current_char_counts:
            # This case should only occur if the input string is empty,
            # but for robustness, we handle it here.
            results.append((i, '', 0))
            continue

        max_count = 0
        max_char = ''

        # List to store characters that currently have the maximum count
        current_max_chars = []

        # Iterate through the characters and their counts in the current prefix
        for c, count in current_char_counts.items():
            if count > max_count:
                max_count = count
                # When a new maximum count is found, reset the list of max characters
                current_max_chars = [c]
            elif count == max_count:
                # If the count is equal to the current max, add the character to the list
                current_max_chars.append(c)

                # If there are multiple characters with the same max_count,
        # choose the alphabetically smallest one as per tie-breaking rule.
        if current_max_chars:
            max_char = min(current_max_chars)
        else:
            # Fallback if no characters have been processed (e.g., empty string case)
            max_char = ''
            max_count = 0

        results.append((i, max_char, max_count))

    return results


# --- Example Usage ---

print("--- Test Case 1: 'banana' ---")
input_str1 = "banana"
result1 = find_max_repeating_char_per_index(input_str1)
for idx, char, count in result1:
    print(f"Index {idx} (prefix '{input_str1[:idx + 1]}'): Max repeating char = '{char}', Count = {count}")
# Expected output for 'banana':
# Index 0 (prefix 'b'): Max repeating char = 'b', Count = 1
# Index 1 (prefix 'ba'): Max repeating char = 'a', Count = 1 (or 'b', depending on tie-breaking. Current code picks 'a' alphabetically)
# Index 2 (prefix 'ban'): Max repeating char = 'a', Count = 1 ('b' or 'n' could also be 1. 'a' is min alphabetically)
# Index 3 (prefix 'bana'): Max repeating char = 'a', Count = 2
# Index 4 (prefix 'banan'): Max repeating char = 'a', Count = 2
# Index 5 (prefix 'banana'): Max repeating char = 'a', Count = 3

print("\n--- Test Case 2: 'programming' ---")
input_str2 = "programming"
result2 = find_max_repeating_char_per_index(input_str2)
for idx, char, count in result2:
    print(f"Index {idx} (prefix '{input_str2[:idx + 1]}'): Max repeating char = '{char}', Count = {count}")

print("\n--- Test Case 3: 'aabbcdefg' ---")
input_str3 = "aabbcdefg"
result3 = find_max_repeating_char_per_index(input_str3)
for idx, char, count in result3:
    print(f"Index {idx} (prefix '{input_str3[:idx + 1]}'): Max repeating char = '{char}', Count = {count}")

print("\n--- Test Case 4: 'mississippi' ---")
input_str4 = "mississippi"
result4 = find_max_repeating_char_per_index(input_str4)
for idx, char, count in result4:
    print(f"Index {idx} (prefix '{input_str4[:idx + 1]}'): Max repeating char = '{char}', Count = {count}")

print("\n--- Test Case 5: Empty String ---")
input_str5 = ""
result5 = find_max_repeating_char_per_index(input_str5)
if not result5:
    print(f"Input: '{input_str5}' -> No results for empty string.")

print("\n--- Test Case 6: Single character string ---")
input_str6 = "z"
result6 = find_max_repeating_char_per_index(input_str6)
for idx, char, count in result6:
    print(f"Index {idx} (prefix '{input_str6[:idx + 1]}'): Max repeating char = '{char}', Count = {count}")

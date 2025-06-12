def find_non_repeating_subsequences(input_string):
    unique_subsequences = set()
    def generate_subsequences_recursive(index, current_subsequence_chars, seen_chars_in_current_subsequence):
        # Base case: If we have processed all characters in the string
        if index == len(input_string):
            # Add the current subsequence to our results.
            # Convert list of chars to a string before adding to the set.
            unique_subsequences.add("".join(current_subsequence_chars))
            return

        # --- Option 1: Exclude the current character ---
        # Don't add input_string[index] to the current subsequence.
        # Move to the next character in the input string.
        generate_subsequences_recursive(
            index + 1,
            list(current_subsequence_chars),  # Pass a copy to avoid modifying for other branches
            set(seen_chars_in_current_subsequence)  # Pass a copy
        )

        # --- Option 2: Include the current character (if it's non-repeating in the current subsequence) ---
        char_to_consider = input_string[index]
        if char_to_consider not in seen_chars_in_current_subsequence:
            # If the character hasn't been seen in the current subsequence, include it.
            current_subsequence_chars.append(char_to_consider)
            seen_chars_in_current_subsequence.add(char_to_consider)

            generate_subsequences_recursive(
                index + 1,
                current_subsequence_chars,
                seen_chars_in_current_subsequence
            )
            # Backtrack: Remove the character and its presence in seen_chars for the next recursive calls
            current_subsequence_chars.pop()
            seen_chars_in_current_subsequence.remove(char_to_consider)

        # Start the recursive process from the first character (index 0)
        # with an empty current subsequence and an empty set of seen characters.

    generate_subsequences_recursive(0, [], set())

print("--- Test Case 1: 'abc' ---")
input_str1 = "abc"
result1 = find_non_repeating_subsequences(input_str1)
print(f"Input: '{input_str1}'")
print(f"Subsequences: {result1}")
# Expected: ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']

print("\n--- Test Case 2: 'banana' ---")
input_str2 = "banana"
result2 = find_non_repeating_subsequences(input_str2)
print(f"Input: '{input_str2}'")
print(f"Subsequences: {result2}")
# Expected to exclude subsequences like 'aa', 'nn', 'nan' etc.

print("\n--- Test Case 3: 'aab' ---")
input_str3 = "aab"
result3 = find_non_repeating_subsequences(input_str3)
print(f"Input: '{input_str3}'")
print(f"Subsequences: {result3}")
# Expected: ['', 'a', 'ab', 'b'] (no 'aa')

print("\n--- Test Case 4: 'level' ---")
input_str4 = "level"
result4 = find_non_repeating_subsequences(input_str4)
print(f"Input: '{input_str4}'")
print(f"Subsequences: {result4}")

print("\n--- Test Case 5: Empty String ---")
input_str5 = ""
result5 = find_non_repeating_subsequences(input_str5)
print(f"Input: '{input_str5}'")
print(f"Subsequences: {result5}")

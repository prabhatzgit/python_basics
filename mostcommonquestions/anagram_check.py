def are_anagrams(str1, str2):
  """Checks if two strings are anagrams (case-insensitive, ignores spaces).

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    True if the strings are anagrams, False otherwise.
  """
  # Remove spaces and convert to lowercase for case-insensitive comparison
  str1 = "".join(str1.split()).lower()
  str2 = "".join(str2.split()).lower()

  # If lengths are different, they cannot be anagrams
  if len(str1) != len(str2):
    return False

  # Method 1: Using sorted()
  # return sorted(str1) == sorted(str2)

  # Method 2: Using character counting (more efficient)
  char_counts = {}
  for char in str1:
    char_counts[char] = char_counts.get(char, 0) + 1

  for char in str2:
    if char in char_counts and char_counts[char] > 0:
      char_counts[char] -= 1
    else:
      return False

  # If all counts are zero, the strings are anagrams
  return all(count == 0 for count in char_counts.values())

# Example Usage
string1 = "listen"
string2 = "silent"
print(f"'{string1}' and '{string2}' are anagrams: {are_anagrams(string1, string2)}")  # Output: True

string3 = "triangle"
string4 = "integral"
print(f"'{string3}' and '{string4}' are anagrams: {are_anagrams(string3, string4)}")  # Output: True

string5 = "hello"
string6 = "world"
print(f"'{string5}' and '{string6}' are anagrams: {are_anagrams(string5, string6)}")  # Output: False

string7 = "Racecar"
string8 = "race car"
print(f"'{string7}' and '{string8}' are anagrams: {are_anagrams(string7, string8)}")  # Output: True

string9 = "Debit Card"
string10 = "Bad Credit"
print(f"'{string9}' and '{string10}' are anagrams: {are_anagrams(string9, string10)}") # Output: True
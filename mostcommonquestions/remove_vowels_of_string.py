def remove_vowels(input_string):
  """Removes all vowels (case-insensitive) from a given string.

  Args:
    input_string: The string from which to remove vowels.

  Returns:
    A new string with all vowels removed.
  """
  vowels = "aeiouAEIOU"
  new_string = ""
  for char in input_string:
    if char not in vowels:
      new_string += char
  return new_string

# Example usage:
text1 = "Hello World"
result1 = remove_vowels(text1)
print(f"Original string: '{text1}'")
print(f"String after removing vowels: '{result1}'")

text2 = "Programming is Fun"
result2 = remove_vowels(text2)
print(f"Original string: '{text2}'")
print(f"String after removing vowels: '{result2}'")

text3 = "AEIOUaeiou"
result3 = remove_vowels(text3)
print(f"Original string: '{text3}'")
print(f"String after removing vowels: '{result3}'")

text4 = "rhythm"
result4 = remove_vowels(text4)
print(f"Original string: '{text4}'")
print(f"String after removing vowels: '{result4}'")
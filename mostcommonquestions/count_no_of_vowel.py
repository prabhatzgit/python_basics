def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0

    for char in input_string:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count

# Test case 1: A simple sentence with mixed case vowels
text1 = "Hello World! This is a test string."
num_vowels1 = count_vowels(text1)
print(f"'{text1}' contains {num_vowels1} vowels.")

# Test case 2: A string with no vowels
text2 = "Rhythm Sky"
num_vowels2 = count_vowels(text2)
print(f"'{text2}' contains {num_vowels2} vowels.")

# Test case 3: A string with all vowels
text3 = "AEIOUaeiou"
num_vowels3 = count_vowels(text3)
print(f"'{text3}' contains {num_vowels3} vowels.")

# Test case 4: An empty string
text4 = ""
num_vowels4 = count_vowels(text4)
print(f"'{text4}' contains {num_vowels4} vowels.")

# Test case 5: String with special characters and numbers
text5 = "Pyth0n Pr0gramm1ng!@#"
num_vowels5 = count_vowels(text5)
print(f"'{text5}' contains {num_vowels5} vowels.")
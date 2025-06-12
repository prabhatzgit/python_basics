def longest_substring(input_string):

    substring=input_string.split()
    if not substring:
        return ""

    longest_string=""
    max_length = 0

    for string in substring:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string

    return longest_string


# Test case 1: A standard sentence
sentence1 = "The quick brown fox jumps over the lazy dog."
longest_word1 = longest_substring(sentence1)
print(f"'{sentence1}' -> Longest word: '{longest_word1}'")

# Test case 2: Sentence with punctuation
sentence2 = "Hello, world! This is a great day."
longest_word2 = longest_substring(sentence2)
print(f"'{sentence2}' -> Longest word: '{longest_word2}'")

# Test case 3: Sentence with numbers and mixed case
sentence3 = "Python is awesome in 2024!"
longest_word3 = longest_substring(sentence3)
print(f"'{sentence3}' -> Longest word: '{longest_word3}'")

# Test case 4: Sentence with multiple words of the same longest length
sentence4 = "apple banana orange grape"
longest_word4 = longest_substring(sentence4)
print(f"'{sentence4}' -> Longest word: '{longest_word4}'") # Should return 'banana' or 'orange' based on order

# Test case 5: An empty string
sentence5 = ""
longest_word5 = longest_substring(sentence5)
print(f"'{sentence5}' -> Longest word: '{longest_word5}'")

# Test case 6: A string with only spaces and punctuation
sentence6 = "   !@#$ %^&  "
longest_word6 = longest_substring(sentence6)
print(f"'{sentence6}' -> Longest word: '{longest_word6}'")

# Test case 7: A sentence with a single word
sentence7 = "Supercalifragilisticexpialidocious"
longest_word7 = longest_substring(sentence7)
print(f"'{sentence7}' -> Longest word: '{longest_word7}'")
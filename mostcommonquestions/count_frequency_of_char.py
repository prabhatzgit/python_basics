def count_frequency(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

my_string = "abracadabra"
char_to_count = "a"
frequency = count_frequency(my_string, char_to_count)
print(f"The frequency of '{char_to_count}' in '{my_string}' is: {frequency}")

def count_char_frequency(text):
    frequency1 = {}
    for char in text:
        frequency1[char] = frequency1.get(char, 0) + 1
    return frequency1

my_string = "hello world"
char_counts = count_char_frequency(my_string)
print(char_counts)
def swap_first_last_char(s):
  if len(s) <= 1:
    return s
  else:
    first_char = s[0]
    last_char = s[-1]
    middle_part = s[1:-1]
    return last_char + middle_part + first_char


word="goa"
print(swap_first_last_char(word))

def swap_first_last_list(s):
    if len(s) <= 1:
        return s
    else:
        char_list = list(s)
        char_list[0], char_list[-1] = char_list[-1], char_list[0]
        return "".join(char_list)

# Example usage (same as above)
string1 = "hello"
swapped1 = swap_first_last_list(string1)
print(f"Original: {string1}, Swapped: {swapped1}")

string2 = "abcde"
swapped2 = swap_first_last_list(string2)
print(f"Original: {string2}, Swapped: {swapped2}")
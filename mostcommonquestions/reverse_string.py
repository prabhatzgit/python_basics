# case1:
# [::-1] creates a reversed copy of the string using slicing.
# The first two colons : indicate that we want to consider the entire string.
# The -1 as the step value indicates that we want to iterate through the string
# in reverse order

string = "hello world"
reversed_string = string[::-1]
print(reversed_string)

# case2: "".join(reversed
# "".join(...) takes the characters yielded by the iterator and
# joins them together using an empty string as the separator,
# effectively creating the reversed string.

reversed_string1 = "".join(reversed(string))
print(reversed_string1)

# case3: for loop
reversed_string2=""
for char in string:
    reversed_string2=char+reversed_string2
print(reversed_string2)

# case4: using recursion

def reverse_string_recursive(s):
    if(len(s)) <= 1:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

given_string = "python"
print(given_string[1:])
reversed_string3 = reverse_string_recursive(given_string)
print(reversed_string3)
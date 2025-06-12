def maximum_consecutive_repeating_character(input_string):
    length = len(input_string)
    max_count = 0
    res = input_string[0]

    # Find the maximum repeating character, starting from s[i]

    for i in range(length):
        count = 0
        for j in range(i, length):
            if input_string[i] != input_string[j]:
                break
            count += 1
        if count > max_count:
            max_count = count
            res = input_string[i]

    return res

s = "aaaabbaaccde"
print(maximum_consecutive_repeating_character(s))


# Python program to find the maximum consecutive
# repeating character in given string

# function to find out the maximum repeating
# character in given string
def maxRepeating(s):
    n = len(s)
    maxCnt = 0
    res = s[0]

    # Find the maximum repeating character
    # starting from s[i]
    i = 0
    while i < n:
        cnt = 1
        while i + 1 < n and s[i] == s[i + 1]:
            i += 1
            cnt += 1

        # Update result if required
        if cnt > maxCnt:
            maxCnt = cnt
            res = s[i]

        i += 1

    return res

# Main function
def main():
    s = "aaaabbaaccde"
    print(maxRepeating(s))

if __name__ == "__main__":
    main()



# Using Counter

# Python program to find the maximum consecutive
# repeating character in given string

# Function to find out the maximum repeating
# character in given string
def maxRepeating(s):
    n = len(s)
    maxCnt = 0
    res = s[0]
    cnt = 1

    for i in range(1, n):

        # If current char matches with
        # previous, increment cnt
        if s[i] == s[i - 1]:
            cnt += 1
        else:

            # Reset cnt
            cnt = 1

        # Update result if required
        if cnt > maxCnt:
            maxCnt = cnt
            res = s[i - 1]

    return res

# Driver Code
s = "aaaabbaaccde"
print(maxRepeating(s))

text="hello"
shift_amount=3
result = ''.join(chr((ord(c)-97 +shift_amount) % 26 +97) for c in text)
print(result)
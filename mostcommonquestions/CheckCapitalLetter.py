def is_valid_capitalization(s):
    if not s:  # Handle empty strings
        return False
    if s.islower() or s.isupper() or (s[0].isupper() and s[1:].islower()):
        return True
    return False

print(is_valid_capitalization("Prabhat"))
print(is_valid_capitalization("prabhat"))
print(is_valid_capitalization("PRABHAT"))
print(is_valid_capitalization("PrABhat"))
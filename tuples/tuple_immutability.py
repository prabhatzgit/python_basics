my_tuple = (10, "apple", 3.14, True)
print(f"Original tuple: {my_tuple}")

# Attempt to change the item's value
try:
    my_tuple[0] = 20
except TypeError as e:
    print(f"\nError when trying to change an item: {e}")

# Attempt to add an item
try:
    my_tuple.append(20)
except AttributeError as e:
    print(f"Error when trying to add an item (append): {e}")

# Another way to attempt adding (concatenation creates a new tuple, doesn't modify the original)
new_element = ("grape",) # Note the comma to make it a tuple
combined_tuple = my_tuple + new_element

print(f"Original tuple after attempted add (no change): {my_tuple}")
print(f"New tuple created by concatenation: {combined_tuple}")

# --- Attempting to remove an item ---
try:
    del my_tuple[1] # This will raise an error
except TypeError as e:
    print(f"Error when trying to remove an item: {e}")

# Attempting to delete the entire tuple (this is allowed, but it deletes the tuple variable itself, not an item within it)
del my_tuple
try:
    print(my_tuple) # This will raise a NameError as my_tuple no longer exists
except NameError as e:
    print(f"Error after deleting the entire tuple: {e}")
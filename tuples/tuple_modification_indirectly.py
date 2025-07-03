original_tuple = (1, 2, 3)
print(f"Original: {original_tuple}")

# To "add" an item: Create a new tuple
new_item = 4
modified_tuple_add = original_tuple + (new_item,) # The comma is crucial for a single-element tuple
print(f"After 'adding' (new tuple): {modified_tuple_add}")

# To "change" an item: Convert to list, modify, convert back to tuple
list_temp = list(original_tuple)
list_temp[0] = 99
modified_tuple_change = tuple(list_temp)
print(f"After 'changing' (new tuple): {modified_tuple_change}")

# To "remove" an item: Create a new tuple by slicing or filtering
# Removing the second element (index 1)
modified_tuple_remove = original_tuple[:1] + original_tuple[2:]
print(f"After 'removing' (new tuple): {modified_tuple_remove}")
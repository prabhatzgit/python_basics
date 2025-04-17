main_string = "Hello Python"
sub_string = "Python"
substring_not_present = "Java"

# case1: using in operator
def check_substring(main_string, sub_string):
    if sub_string in main_string:
        print(f"{main_string} contains {sub_string} ")
    else:
        print(f"{main_string} does not contain {sub_string} ")

print(check_substring(main_string, sub_string))

# case2: using the find() method

def check_substring_index(main_string, sub_string):
  index = main_string.find(sub_string)    
  if index != -1:
      print(f"{sub_string} found at index {index} of {main_string}")
  else:
      print(f"{sub_string} not found at index {index} of {main_string}")

print(check_substring_index(main_string, sub_string))

def check_substring_index_one(main_string, substring_not_present):
    index_one = main_string.find(substring_not_present)
    if index_one != -1:
        print(f"{substring_not_present} found at index {index_one} of {main_string}")
    else:
        print(f"{substring_not_present} not found at index {index_one} of {main_string}")

main_string_index = "Python is fun"
sub_string_index = "is"

try:
    index_two = main_string_index.index(sub_string_index)
    print(f"{sub_string_index} found at index {index_two}")
except:
    print(f"{sub_string_index} not found")

substring_not_present_index = "Java"
try:
    index_three = main_string_index.index(substring_not_present_index)
    print(f"'{substring_not_present_index}' found at index {index_three}")
except ValueError:
    print(f"'{substring_not_present}' not found")    
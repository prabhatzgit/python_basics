def format_name(f_name, l_name):
    """Take a first name and last name and format it to return the title case
    version of the name""" # this is docstrings
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_first_name = f_name.title() # convert prabhat to Prabhat
    formatted_last_name = l_name.title()
    return f"Result: {formatted_first_name} {formatted_last_name}"

print(format_name(input("What is your first name?"),input("What is your last name?")))
# print(formatted_string)

def function_one(text):
    return text + text

def function_two(text):
    return text.title()

output = function_two(function_one("hello"))
print(output)
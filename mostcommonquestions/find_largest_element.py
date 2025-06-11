def find_largest_element(input_list):
    largest = input_list[0]
    for element in input_list:
        if element > largest:
            largest = element
    return largest

# Test the function
given_list = [10,5,8,20,3]
largest_number = find_largest_element(given_list)
print(f"largest number is {largest_number}")
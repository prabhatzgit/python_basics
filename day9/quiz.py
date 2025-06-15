# quiz 1
starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
print(starting_dictionary == final_dictionary)

# quiz 2
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# option 1
dict["c"] = [1, 2, 3] # update the values in key "c"

print(dict)

# quiz 3

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2])
print(order["main"][2][0])
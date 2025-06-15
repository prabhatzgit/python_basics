colors = {
"apple" : "red",
"pear" : "green",
"banana" : "yellow"
}

# key "apple" exists and print value "red"
print(colors["apple"])

# key "mango" does not exist and print error -- KeyError: 'mango'
#print(colors["mango"])

# this below line will create a pair and insert in the dictionary
colors["guava"] = "green"
print(colors)

# Edit an item in a dictionary
colors["apple"] = "mixed colour of red and yellow"
print(colors)

# Wipe an existing dictionary
# colors = {}
# print colors

# Loop through a dictionary
# color - key
for color in colors:
    print(color)
    print(colors[color])
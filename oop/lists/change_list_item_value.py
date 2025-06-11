# Change item value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a range of item values

# To change the value of items within a specific range,
# ["banana", "cherry"]
#  define a list with the new values, 
# thislist[1:3] = ["blackcurrant", "watermelon"]
# and refer to the range of index numbers where you want to insert the new values

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

thislist[1:2] = ["Guava","pear","Grapes"]
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingl

listone = ["apple", "banana", "cherry"]
listone[1:3]=["watermelon"]
print(listone)
print(len(listone))

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index

insertlist = ["apple", "banana", "cherry"]
insertlist.insert(2, "blackcurrant")
print(insertlist)
# Range function with For Loop

for number in range(1, 100):
    print(number)

for number in range(1, 100, 3): # add 3 to the next print element
    print(number)

total = 0
for number in range(1, 100):
    total += number
    print(total)
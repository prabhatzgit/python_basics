import random
import my_module

random_integer = random.randint(10,20)
print(random_integer)

print(my_module.my_favourite_number)

# random - Returns a random float number between 0 and 1
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# uniform() - returns a random floating number between the two
# specified numbers (both included)
random_float = random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
# -----------

scorePlus = 0
scoreMinus = 0
# Users score a point
scorePlus += 1 #score = score +1
scoreMinus -= 1 #score = score -1
print(scorePlus)
print(scoreMinus)

# f-strings
print("Your score is : " + str(scorePlus))

score = 0;
height = 1.8
is_winning = True

print(f"Your score is :  + {score}, your height is {height}. You are winning is {is_winning}")
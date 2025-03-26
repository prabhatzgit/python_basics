# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.
# This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6.

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = (weight / (height * height) )
bmi_1 = 84 / 1.65 ** 2

print(bmi)
print(bmi_1)

print(int(bmi_1)) # skip decimal value and answer is 30

print(round(bmi_1)) # rounds to figured value 30.85399449035813 --> 31

print(round(bmi_1, 2)) # 30.85399449035813 --> 30.85
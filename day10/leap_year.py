def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2400))
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    love_score = int(str(true_count) + str(love_count))

    print(f"Your love score is: {love_score}")
    return love_score

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

calculate_love_score(name1, name2)
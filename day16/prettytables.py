from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Tech stack", ["Java", "Python", "React", "Angular"])
table.add_column("Type",["Backend","Backend","Frontend","Frontend"])

print(table.align)

table.align = "l"
print(table)


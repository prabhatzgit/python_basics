def replace_all_occurences(main_string, sub_string_exist, sub_string_replace):
  new_string = main_string.replace(sub_string_exist, sub_string_replace)
  return new_string

main_string = "Hello Java"
sub_string_exist = "Java"
sub_string_replace = "Python"
new_string = replace_all_occurences(main_string, sub_string_exist, sub_string_replace)
print(new_string)

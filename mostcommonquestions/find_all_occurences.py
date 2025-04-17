def occurences_of_substring_in_a_string(main_string, sub_string):
  indices = []
  start = 0
  while True:
    index = main_string.find(sub_string, start)
    if index == -1:
      break
    indices.append(index)
    start = index + 1
  return indices

main_string = "This is a test string with the word test repeated."
sub_string = "test"
occurences = occurences_of_substring_in_a_string(main_string, sub_string)

print(f"occurences of {sub_string} found at indices: {occurences} of {main_string}")

phrase = input(' ')
occurrences = phrase[1:-1]
char_to_count = phrase[0]
occurrences = occurrences.count(char_to_count)
occurrences_str = str(occurrences)
print('{}'.format(occurrences_str))

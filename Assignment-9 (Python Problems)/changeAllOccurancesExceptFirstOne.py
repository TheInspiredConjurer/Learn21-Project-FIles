def changeAllOccurancesExceptFirstOne(str1):
  char = str1[0]
  str1 = str1.replace(char, '*')
  str1 = char + str1[1:]

  return str1

print("\nOriginal String: babble")
print("Transformed String:",changeAllOccurancesExceptFirstOne('babble'))
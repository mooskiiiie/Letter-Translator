def translate(word):
  translation = ""
  for letter in word:
    if letter.lower() in "aeiou":
      if letter.isupper():
        translation += "G"
      else:
        translation += "g"
    else:
      translation += letter
  return translation
  
 print(translate(input("Enter word: ")))

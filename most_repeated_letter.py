text = "This is a common interview question"

dict = {letter:0 for letter in text if letter != ' '}

for l in text:
    if l != ' ':
        dict[l] += 1

print(f"Most repeated character in the text is '{sorted(dict.items(), key = lambda x:x[1], reverse = True)[0][0]}', "
      f"it repeats {sorted(dict.items(), key = lambda x:x[1], reverse = True)[0][1]} times")

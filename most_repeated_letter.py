#    This program finds the most repeated letter in the string.

text = "This is a common interview question"

dict = {letter:0 for letter in text if letter != ' '}    # Here I'm using comprehension to create dictionary, where letters are keys, and their quantities are values

for l in text:    # Here I'm going through the string using a loop and count how many and what letters the string has
    if l != ' ':
        dict[l] += 1

print(f"Most repeated character in the text is '{sorted(dict.items(), key = lambda x:x[1], reverse = True)[0][0]}', "    # Here I'm retrieving keys and values of my dictionary with itmes() method
      f"it repeats {sorted(dict.items(), key = lambda x:x[1], reverse = True)[0][1]} times")                             # then I'm using the lambda function that returns quantities of letters
                                                                                                                         # then I'm sorting my dictionary by letters quantities with reverse flag 
                                                                                                                         # and getting the first item of my sorted dictionary

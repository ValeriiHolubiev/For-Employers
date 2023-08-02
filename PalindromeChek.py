# This simple program will check if given text is palindrome or not.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.

T = input("Enter text: ").replace(' ' and '\t', '')

for i in range(len(T)):
	T1 = T[i]
	T2 = T[(i+1)*-1]
	
	if T1.lower() == T2.lower():
		isPalinrome = True

	else:
		isPalinrome = False
		break

if isPalinrome:
	print(T + ' is Palindrome!')

else:
	print(T + ' isn\'t Palindrome!')
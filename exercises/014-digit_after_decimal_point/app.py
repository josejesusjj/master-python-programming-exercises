#Complete the function to return the first digit to the right of the decimal point.
def first_digit(num):
	string = str(num)
	for i in range(len(string)):
		if string[i] == '.':
			return int(string[i + 1])



#Invoke the function with a positive real number. ex. 34.33
print(first_digit(6.24))
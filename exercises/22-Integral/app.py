# Your code here
def generate_dict(n): 
	dictionary = {}
	for i in range(1,n+1):
		integral = i * i		
		dictionary[i]=integral
	return dictionary

print(generate_dict(8))
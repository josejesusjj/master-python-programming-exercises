#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  return int(str(num%10)+str(int(num/10))) 
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))

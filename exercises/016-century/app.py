#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math
def century(year):
  century = ((year - 1)/100)+1
  return int(century)



#Invoke the function with any given year. 
print(century(3022))
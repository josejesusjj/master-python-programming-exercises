#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
  h = int(n/60)
  m = n%60
  return h,m

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
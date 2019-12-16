# import the randint function from the random module
from random import randint

# create a function to generate a list of "size" random integers
# up to a maximum of largest"

def random_list(largest,size):
  # create an empty list
  l = []
  # add a random number to the list the number of times
  for i in range(size):
    n = randint(0,largest-1)
    l.append(n)
  #print the list to check
  return(l)
#call the function
l = random_list(10,10)

print(l)

num1 = input("Choose a value from the list above: ")

def find_number(l, num1):
  z = 0
  for i in l:
    if(int(num1) == i):
     z+=1
  return z

z = find_number(l, num1)
print(z)

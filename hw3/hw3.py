
from datetime import date

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light=="red":
        return "stop"
    elif light=="green":
        return "go"
    elif light=="yellow":
        return "wait"
    else:
       raise Exception(f"Undefined instruction for color: {light}")

#print(car_at_light("red"))
print(car_at_light("yellow"))
# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 
def safe_subtract(a, b):
    try:
        return a - b
    except TypeError:
        return None
    except Exception as e:
        print(f"Error: {e}")
print(safe_subtract(2, 3))        
  


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that return the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl
people = [{'name': 'John', 'last_name': 'Doe', 'birth': 1987},
{'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}]
def retrieve_age_eafp(person):
    try:
        return date.today().year - person['birth']
    except KeyError:
        return None

def retrieve_age_lbyl(person):
    if 'birth' in person:
        return date.today().year - person['birth']
    else:
        return None

for person in people:
    print(person['name'], retrieve_age_eafp(person), retrieve_age_lbyl(person))

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that takes the path to the file as an argument
# and reads the file making sure to use to handle the fact
# that it might not exist. 
#

def read_data(path):
    try:
       with open(path) as f:
           return f.read()
    except FileNotFoundError:
        print(f"No file found")
        return None
print("The file exists? ", read_data("data.csv"))
# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem
#Bug: We calculate `double` but never use it. The line adds `elem`
#      (the original number) instead of `double`.
#      Result: 17 (10 + 5 + 2) instead of 34 (20 + 10 + 4).
# FIX: Add `double` to the total, not `elem`.
total_double_sum= 0
for elm in [10, 5, 2]:
    double = elm * 2
    total_double_sum +=double
print(total_double_sum) 
# it should print 34

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string
#Bug 1: strings overwrites the variable on every loop, so only last word is kept.
# Bug 2: strings joins itself hence it will print "Groot_Groot"
# instead of adding the word to that was already built. 
# FIX: Add each new word to what we already have in `strings`.
strings = '' 
for string in ['I', 'am', 'Groot']:
    strings = strings + string + "_"

print(strings)
# Result: 'I_am_Groot_'

### (c) Careful!
# j=10
# while j > 0:
#    j += 1
# Bug: j starts at 10 and j += 1 makes it grow 
# so j>0 is always true and loop never ends(infinite loop).
# Fix: Count down should decrement until j reaches 0 and the loop stop. 
j =10
while j> 0:
    j-=1
print(j) 
# result: 0

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem
# Bug: Productory starts at 0 and any number time 0 is 0.
# Hence the results are always 0.
# Fix: start at 1
productory = 1
for elm in [1, 5, 25]:
    productory*= elm
print(productory)
# result:125


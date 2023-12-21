#!/bin/python3

#variables and methods
# edit on 21.12.2023

quote = "All is fair in love war."
print (quote)
print (quote.upper()) # upper cases
print (quote.lower()) # lower cases
print (quote.title()) # title cases
print (len(quote)) # string length

name = "Murat" # string
age = 30 # int
gpa = 3.7 # float
print (age)
print (int(30.9))
print("my name is  " + name + " and I am " + str(age) + " years old")

age = age + 2
print(age)

three = 3
age += three
print(age)

print('\n')
# functions
print("here is an example for function: ")

def who_am_i(): # this is a function
	name = "Murat"
	age = 30
	print("my name is  " + name + " an I am " + str(age) + " years old")

who_am_i()
print(age)

#adding parameters

def add_one_hundred(num):
	print(num + 100)

add_one_hundred(50)

#multiple parameters
def add(x,y):
	print(x+y)
add(10, 6)

def multiply(x,y):
	return(x*y)
print(multiply(4,5))

def square_root(x):
	print(x ** .5)
square_root(81)

def nl(): # new line
	print('\n')

nl()

#Boolean expressions (True or False)
print ("Boolean expressions: ")
bool1 = True
bool2 = 3*3 == 9 # will return True
bool3 = False
bool4 = 3*3 !=9 # will return false
print(bool1, bool2, bool3, bool4)
print(type(bool1))

# relational and bolean operationa
greater_than = 7>5
less_than = 5<7
greater_than_or_equal = 7>= 7
less_than_or_equal = 7<= 7
test_and = (7>5) and (5<7) # true
test_and2 = (7>5) and (5<7) # true
test_or= (7>5) and (5<7) # true
test_not = not True # false

nl()
# conditional statements

def drink(money):
	if money >= 2:
		return "you've got the drink!"
	else:
		return "No drink for you!"
print(drink(3))
print(drink(1))

def alcohol(age, money):
	if (age >=21) and (money >=5) :
		return " we get a achohol drink!"
	elif (age >=21) and (money < 5) :
		return " come back with more money!"
	elif (age < 21) and (money >= 5) :
		return "Nice try, kid! "
	else:
		return "you're too poor and too young!"

print(alcohol(21,5))
print(alcohol(20,5))
print(alcohol(2,3))

nl()
# Lists - have brackets []
movies = ["When Harry met Sally", "The Hangover", " The perks of Being Wallflower", "The Excorcist"]
print (movies[1]) # prints The Hangover
print (movies[0]) # prints When Harry met Sally
print(movies[1:3]) # printing start with the 1st element and stops at the 3rd element. So it prints The Hangover and The perks of Being Wallflower
print(movies[1: ]) # printing start with the 1st element and all the rest it prints as well
print(movies[ :2]) #printing start with the first element \(0\) and stops at the 2nd element
print(movies[-1]) # prints the last element 
print (len(movies))
movies.append("JAWS")
print(movies)
movies.pop() # pop deletes the last element in the list!
print(movies)
movies.pop(0)
print(movies)

football_teams = ["GS", "FB", "TS", "KS", "Bayern"]
print(football_teams)
print(football_teams[1: ])






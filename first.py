import random 
import os
import shutil


name = "Bro Code"

first_name = name[:3]
last_name = name[4:8]
funky_name = name[::2]
reversed_name = name[::-1]

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)
a = website1[slice]

#set = collection which is unordered, unindexed. No duplicate values
utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup", "knife"}

utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# dictionary = A changeble, unordered collection of unique key: value pairs. Fast because tehy use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'
        }

# print(capitals['India']) //New Dehli
# print(capitals.keys())   //or .values() or .items()

# for key, value in capitals.items():
    # print(key, value)

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})

# index operator [] = gives access to a sequence's element (str, list, tuples)

name = 'bro Code'

# if(name[0].islower()):
    # name = name.capitalize()

first_name = name[:3].upper() #BRO
last_name = name[4:].lower() #code
last_character = name[-2] #d

#function = a block of code which is executed only when it is called.

def hello(word):
    print(f"hellow {word}")
    return
name = "biksbee"
# hello(name)

# return statement = Functions send Python values/objects back to the caller. These value/objects are known as the function's return value

# keyword arguments

def hello(first,middle,last):
    a = first+' '+middle+' '+last
    print(a)

# hello(last='A',middle='B',first='C')

# nested functions calls = function calls inside other function calls innermost function calls are resolved first returned value is used as argument for the next outer function

# *args = parameter that will pack all arguments into a tuple

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

# print(add(1,2,3,4,5,6))

# **kwargs

def hello(**kwargs):
    print("Hello " + kwargs['first'] + ' ' + kwargs['last'])
    for key, value in kwargs.items():
        print(key, end=" ")

# hello(first='bro', last='code', title='Mr.')

number = 1000

# print('The number is {:b}'.format(number))

# random number

x = random.randint(1,6)
y = random.random()
myList = ['a', 'p', 's']
random.shuffle(myList)

# print(myList)

# exception = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print("You can't divide by zero!")
#     print(e)
# except ValueError as e:
#     print("Enter only numbers")
#     print(e)
# except Exception as e:
#     print("something went wrong:(")
#     print(e)
# else: 
#     print(result)
# finally: 
#     print("this will alwys execute")

path = "/home/biksbee/programming/python/lessons/"

# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
# else: 
#     print("That location doesn't exists!")

# try:    
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found:( ")

# text = 'Have a nice day! See ya'

# with open('test.txt', 'a') as file:
#     file.write(text)

# shutil.copyfile('test.txt', 'copy.txt') #src, dst
# shutil.copy('test.txt', 'copy.txt') #src, dst
# shutil.copy2('test.txt', 'copy.txt') #src, dst

# choices = ["rock", "paper", "scissors"]

# computer = random.choice(choices)
# player = None

# while player not in choices:
#     player = input("rock, paper, or scissors?").lower()

# print("computer: ", computer)
# print("palyer: ", player)
# if player == computer:
#     print("Tie!")
# elif player == "rock":
#     if computer == "paper":
#         print("You lose!!")
#     if computer == "scissors":
#         print("You win!")
# elif player == "scissors":
#     if computer == "rock":
#         print("You lose!!")
#     if computer == "paper":
#         print("You win!")
# elif player == "paper":
#     if computer == "scissors":
#         print("You lose!!")
#     if computer == "rock":
#         print("You win!")

foods = list()

while food := input("What food do you like?: ") != 'quit':
    foods.append(food)

# print(foods)
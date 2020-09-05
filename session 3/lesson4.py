# use elif for if code with more than 2 conditions.
# a=300
# b=200
# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is smaller than b")
# else:
#     print("a í equal to b")

# nhỏ/lớn hơn hoặc bằng: >=, <=
# from math import*
# a=int(input("Enter your number"))
# b=int(input("Enter your number"))
# c=int(input("Enter your number"))
# if a==b or b==c or a==c:
#     print("Tam giác cân")
# elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2:
#     print("Tam giác vuông")
# else:
#     print("Tam giác thuờng")
# s = (a+b+c)/2
# area = s*(s-a)*(s-b)*(s-c)
# print(int(sqrt(area)))

# example: book.lower => convert text from user input into lowercase 
# Boolean: not True là False, not False là True
# books = ["book 1","book 2", "book 3","book 4"]
# while True:
#     userInput = input("Enter here: ")
#     # for book in books:
#     #     if userInput == book.lower():
#     #         print(book)
#     #         break
#     #     else:
#     #         print("Not found:(")
    
#     if userInput in books:
#         index = books.index(userInput)
#         print(books[index])
#         break 


# Codes for this one game called Freakingmath
# randrange: random number from a specific range 
from random import *
a=randrange(10)
b=randrange(10)
correct=a+b
wrongNumber=[-1,0,1]
incorrect= correct+choice(wrongNumber)
# choice code: random pick from list wrongNumber
print(a, "+", b, "=", incorrect)
userInput = input("True or False (T/F): ")
if correct != incorrect:
    if userInput.lower() == "t":
        print("You lose")
    else:
        print("You win") 
if correct == incorrect:
    if userInput.lower() == "t":
        print("You win")
    else:
        print("You lose") 


    









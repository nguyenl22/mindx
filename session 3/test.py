# part 1
# q1
a=input("Enter your full name:")
print(a)

# q2
a=input("Enter your full name:")
print(a.upper())

# q3
a=int(input("Enter your number"))
print(a**2)

# q4
a=int(input("Enter circle's radius"))
from turtle import*
circle(a)

# part2
# q1
for i in range(3,13,1):
    print(i)

# q2
a=int(input("Enter your positive number"))
for i in range(0,a+1,1):
    print(i)

# q3
a=int(input("Enter your positive odd number"))
print(0)
for i in range(1,a+2,2):
    print(i)

# q4
a=int(input("Number of polygon's edge"))
from turtle import*
for i in range(a):
    forward(100)
    right(360/a)

# part3
# q1
a=int(input("Enter your number"))
if a>13:
    print("Larger than 13")
elif a<13:
    print("Smaller than 13")
else:
    print("Equals to 13")

# q2
a=int(input("Enter your number"))
if a%2==0:
    print("Even")
else:
    print("Odd")

# # q3
a=int(input("Enter your month"))
if a in [1,3,5,7,8,10,12]:
    print("31 days")
elif a in [4,6,9,11]:
    print("30 days")
elif a==2:
    print("28 days")

#part4
# q1
username=input("Enter your username")
password=input("Enter your password")
email=input("Enter your email")

# q2
username=input("Enter your username")
username2=input("Re-enter your username")
while username != username2:
    username2=input("Re-enter your username")
password=input("Enter your password")
email=input("Enter your email")

# q3
username=input("Enter your username")
username2=input("Re-enter your username")
while username != username2:
    username2=input("Re-enter your username")
password=input("Enter your password")
while len(password)<9:
    password=input("Password must contain more than 8 characters. Re-enter password.")
while password.isalpha() or password.isdigit():
    password=input("Password must contain both numbers and letters. Re-enter password.")
email=input("Enter your email")
while "@" and "." not in email:
    email=input("Invalid, re-enter email")











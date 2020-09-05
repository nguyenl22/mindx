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
    
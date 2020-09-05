# q1
for i in range(0,7,1):
    print(i, end="")
for i in range(100,106,1):
    print(i, end="")
for i in range(9,1,-1):
    print(i, end="")

# q2
for i in range(0,21,1):
    print(i)

# q3
n=int(input("Enter your number:)"))
for i in range(0,n+1,1):
    print(i)

#  q4
for i in range(5,13,1):
    print(i)

# q5
from turtle import*
fillcolor('yellow')
begin_fill()
color('green')
circle(100)
end_fill()

#  q6
from turtle import*
color('green')
for i in range(6):
    circle(100)
    right(60)

#  q7
n=int(input("Enter your number:)"))
a=(n+1)*n/2
print(a)

# q8
n=int(input("Enter your number:)"))
if n==5:
    n=int(input("Lmao choose another one dumbo"))
if n>5:
    for i in range(5,n+1,1):
        print(i)
if n<5:
    for i in range(5,n-1,-1):
        print(i)

#  q9
for i in range(20,11,-1):
    print(i)

# q10
n=int(input("Enter your 1st number."))
m=int(input("Enter your 2nd number."))
if n>m:
    for i in range (n,m-1,-1):
        print(i)
else:
    print("Error")

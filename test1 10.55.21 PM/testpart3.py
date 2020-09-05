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
# # part3
# # q1
# a=[1,2,3,4,5]
# b=int(input("Enter your number: "))
# if b in a:
#    print("Found, position: ", a.index(b)+1)
# else:
#     print("Not found in our list")
# # q2
# c=[23,45,67]
# print("Sum of all numbers: ", sum(c))
# total=0
# for item in c:
#     total += item
# print("Sum of all numbers: ", total)
# q3
d=input("Enter your list of numbers, separated by a space")
e=d.split()
f=map(int,e)
print("Sum of all numbers: ", sum(f))
    

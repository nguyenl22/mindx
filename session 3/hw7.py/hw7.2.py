# part2
# q1
a=['red','blue','yellow','orange']
user=int(input("Enter color position:"))
print(a[user - 1])
# q2
a=['red','blue','yellow','orange']
print('Our color list:')
for i in range(len(a)):
    print(i+1, a[i])
user=input("Enter item for deletion:")
print("Item to delete: ", user)
print("Our new color list:")
if user.isdigit():
    a.pop(int(user)-1)
if user.isalpha():
    a.remove(user)
for i in range(len(a)):
    print(i+1, a[i])
# q3
from turtle import*
for i in range(len(a)):
    pencolor(a[i])
    forward(100)










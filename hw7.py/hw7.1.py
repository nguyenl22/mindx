# part1
# q1
a=['red','blue','yellow']
# q2
print('Our color list:')
for i in range(len(a)):
    print(a[i], end=",")
# q3
b=input("Enter your color")
a.append(b)
print('Our color list:')
for i in range(len(a)):
    print(a[i], end=",")
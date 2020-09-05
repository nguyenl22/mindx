# part4
# q1
a=[34,5,6,22,7]
for item in a:
    if item%2 != 0:
        a.remove(item)
print("All even numbers are:")
for i in range(len(a)):
    print(a[i], end=",")
# q2
b=input("Enter your numbers:")
a=b.split(',')
for item in a:
    if int(item)%2 != 0:
        a.remove(item)
print("All even numbers are:")
for i in range(len(a)):
    print(a[i], end=",")
    

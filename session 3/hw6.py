# q2
sheepsize=[4,2,3,7,8,9]
print("These are my sheeps' sizes:") 
print(sheepsize)
biggestsheep=max(sheepsize)
print("Let's shear our biggest sheep, whose size is", biggestsheep)
sheepsize[sheepsize.index(biggestsheep)]=8
print("After shearing, here is my flock", sheepsize)
print("One month has passed now here is my flock")
for i in range(len(sheepsize)):
    sheepsize[i]=sheepsize[i]+50
print(sheepsize)
for i in range (4):
    biggestsheep=max(sheepsize)
    sheepsize[sheepsize.index(biggestsheep)]=8
    print("Month", i+1)
    print("One month has passed now here is my flock")
    for i in range(len(sheepsize)):
# sheepsize[i]=sheepsize[i]+50 is similar to sheepsize[i]+= 50
        sheepsize[i]=sheepsize[i]+50
    print(sheepsize)
sum=sum(sheepsize)
print("My flock has a total size of"), print(sum)
print("Profit is"), print(sum*2)

# max code simplified: bruh this is actually smart
max_size=0
for size in sheepsize:
    if size>max_size:
        max_size=size
print(max_size)
# sum code simplified:
total=0
for item in sheepsize:
    total += item
print(total)

# q3
# shuffle 
from random import*
word="apple"
word= list(word)
shuffle(word)
for w in word:
    print(w, end="")
# end="" thì output được in ngang, end="abcd" thì space được replaced bằng abcd

# shuffle code explained; bruh this is actually smart
list=['a','b']
temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)









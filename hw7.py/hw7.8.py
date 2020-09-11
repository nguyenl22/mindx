# q1
highscores=[45,67,56,78]
a=[]
for i in range(len(highscores)):
    a.append(max(highscores))
    highscores.remove(max(highscores))
print('High scores:')
for i in range(len(a)):
    print(i+1, a[i])
# q2
highscores=[45,67,56,78]
while True:
    b=int(input("Enter your new score:"))
    highscores.append(b)
    a=[]
    for i in range(5):
        a.append(max(highscores))
        highscores.remove(max(highscores))
    print('High scores:')
    for i in range(len(a)):
        print(i+1, a[i])
    highscores=a

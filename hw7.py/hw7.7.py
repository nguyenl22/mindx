# q1
highscores=[45,67,56,78]
# q2
print('High scores:')
for i in range(len(highscores)):
    print(i+1, highscores[i])
# q3
a=int(input("Enter your new score:"))
highscores.append(a)
print('High scores:')
for i in range(len(highscores)):
    print(i+1, highscores[i])

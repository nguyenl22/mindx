# q1
computer={
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
for key, value in computer.items():
    print(key,":",value)

# q2
computernumber=[]
for item in computer:
    computernumber.append(computer[item])
print(sum(computernumber))

# q3
computer.update({"FUJITSU":15})
computer.update({"ALIENWARE":5})


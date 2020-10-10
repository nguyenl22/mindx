# q1
computer={
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

# q2
numbermac=computer["MACBOOK"]
print("The number of Macbook is", numbermac)

# q3
userinput=input("Enter computer type in all caps:")
if userinput in computer:
    print("The number of", userinput, "is:", computer[userinput])
else:
    print("Not found")


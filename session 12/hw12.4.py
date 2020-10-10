# q1
computer={
    "HP": 600,
    "DELL": 650,
    "MACBOOK":12000,
    "ASUS": 400,
    "ACER":350,
    "TOSHIBA":600,
    "FUJITSU":900,
    "ALIENWARE":1000
}

# q2
print("The price of an ASUS is:", computer["ASUS"])

# q3
userinput=input("Enter computer type in all caps:")
if userinput in computer:
    print("The price of a", userinput, "is:", computer[userinput])
else:
    print("Not found")

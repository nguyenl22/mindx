# q1
computer={
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
computer.update({"TOSHIBA":10})

# q2
userinput1=input("Enter computer type in all caps:")
userinput2=int(input("Enter number of computer:"))
computer.update({userinput1:userinput2})

# q3
computer["DELL"]+=10
computer["MACBOOK"]+= -2






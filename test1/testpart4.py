# #part4
# # q1
# username=input("Enter your username")
# password=input("Enter your password")
# email=input("Enter your email")

# # q2
# username=input("Enter your username")
# password=input("Enter your password")
# password2=input("Re-enter your password")
# while password != password2:
#     password2=input("Re-enter your password")
# email=input("Enter your email")

# q3
username=input("Enter your username")
password=input("Enter your password")
while password.isalpha() or password.isdigit():
    password=input("Password must contain both numbers and letters. Re-enter password.")
while len(password)<9:
    password=input("Password must contain more than 8 characters. Re-enter password.")
password2=input("Re-enter your password")
while password != password2:
    password2=input("Re-enter your password")
email=input("Enter your email")
while "@" and "." not in email:
    email=input("Invalid, re-enter email")
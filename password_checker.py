MIN_LENGTH = 2
symbol = "*"

print("enter a valid password")
print("your password must be longer then", MIN_LENGTH)
password = input("")
password_length = len(password)
if password_length > MIN_LENGTH:
    print(symbol * password_length)
else:
    print("Password is too short")

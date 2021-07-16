a = input("What is your name")
b = input("How much do you earn")
if int(b)==0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isnumeric() or a.isalnum():
    raise Exception("Numbers are not allowed")

print(f"Hello {a}")
# 1000 lines taking 1 hour

# Task - Write about 2 built in exception

# c = input("Enter your name")
# try:
#     print(a)
#
# except Exception as e:
#
#     if c =="virat kohli":
#         raise ValueError("virat kohli is blocked he is not allowed")
#
#     print("Exception handled")
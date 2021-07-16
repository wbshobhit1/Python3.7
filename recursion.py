# def fibonacci(n):
#     if n is 0:
#         return 0
#     elif n is 1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# number = int(input("Enter the number "))
# print("The fibonacci number is ", fibonacci(number))
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c= a+b
        a,b = b,c
    return a


number = int(input("Enter the number "))
print("The fibonacci number is ", fibonacci(number))

# def factorial(n):
#     if n is 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# number = int(input("Enter the number "))
# print("The factorial number is ", factorial(number))

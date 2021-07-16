"""""
 print("Enter the age of the person")
age = int(input())

if age > 18:
    print("You are eligible to drive")

elif age == 18:
    print("Physical Apperance needed")

elif age < 4 and age < 125:
    print("bhai se jhoot bolega ab sach bta age ye maii nhi maan raha")

else:
    print("chala jaaa bsdk ")
"""
# Excercise 2- Faulty Calculator

print("Enter the two numbers on which we have to apply operation")
a = int(input())
b = int(input())
print("Select the operator ")
c = input()
l = ["+", "-", "*", "/"]


if c == "+":
    if a == 56 and b == 9:
        print(77)
    elif a == 9 and b == 56:
        print(77)
    else:
        print(a+b)

elif c == "-":
    print(a-b)

elif c == "*":
    if a == 45 and b == 3:
        print(555)
    elif a == 3 and b == 45:
        print(555)
    else:
        print(a*b)
elif c not in l:
    print("enter valid operation")

else:
    if a == 56 and b == 6:
        print(4)
    else:
        print(a/b)

print("thanks for using calc")
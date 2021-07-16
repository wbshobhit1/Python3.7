# print(0 | 2)

# Excercise 4
try:
    print("Input the number")
    n = int(input())
    print("Type 0 OR 1")
    boolean = int(input())
    check = bool(boolean)
    if check:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
    elif not check:
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print("*", end=" ")
            print()
except Exception as e:
    print('invalid entry')


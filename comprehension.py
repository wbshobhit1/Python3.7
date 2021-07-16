# """"
# List Comprehensions
# """
# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)
#
# """"
# Dictionary  Comprehensions
# """
# dict1 = {
#     i: f"Item{i}" for i in range(1, 101)
#     if i % 5 == 0
# }
# dict2 = {
#     value: key
#     for key, value in dict1.items()
# }
# print(dict1, "\n", dict2)
#
# """"
# Set  Comprehensions
# """
# dresses = {dress for dress in ["dress1", "dress2", "dress1",
#                                "dress2", "dress1", "dress2"]}
# print(type(dresses))
# print(dresses)
#
# """"
# Generators Comprehensions
# """
# evens = (i for i in range(100) if i % 2 == 0)
# print(type(evens))
# # print(evens.__next__())
# # print(evens.__next__())
# # print(evens.__next__())
# print(tuple(evens))

#  Question On comprehension:-

n = int(input("Enter how many input you want to take :\n"))
while True:
    print("Which comprehension you want to select")
    print("1.List\n2.Dictionary\n3.Set")
    inp = input()

    if inp not in ['1', '2', '3']:
        print("😞 Please enter a valid option 😞")
        continue
    else:
        inp = int(inp)

    if inp == 1:
        ls = [i for i in range(n)]
        print(ls)

    elif inp is 2:
        dict1 = {
            i: f"Item{i}" for i in range(n)
        }
        dict1 = {
            value:key
            for key,value in dict1.items()
        }
        print(dict1)

    elif inp is 3:

        set1 = {i for i in range(n)}

    print("Press Q to quit OR C to continue")

    opt1 = ""
    while (opt1 != "q" and opt1 != "c") or (opt1 != "q" and opt1 != "c"):
        opt1 = input()
        if opt1 == "q" or "Q":
            break
        elif opt1 == "C" or "c":
            continue


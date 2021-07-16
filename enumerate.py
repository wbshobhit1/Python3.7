# Normal type By declaring variables
# When we have to leave even or odd items
"""""
l1 = ["Boult", "Bhumrah", "Smith", "Rabada", "Pant"]

i = 1
for item in l1:
    if i % 2 is not 0:
        print(f"{item} Will win a bet for u")
    i += 1
"""


# Using enumurate Functions, We can skip the variables part that we put

l1 = ["Boult", "Bhumrah", "Smith", "Rabada", "Pant"]


for index, item in enumerate(l1):
    if index % 2 is 0:
        print(f"{item} Will win a bet for u")

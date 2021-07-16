"""""
l1 = [["bugati", 4], ["audi", 387], ["jaguar", 141], ["land rover", 387], ["bmw", 847]]

d1 = dict(l1)
for item in d1:
    print("total number of "+item)
"""
# quiz
l= [int, float, "ramdi", 4, 7, 9, 2, 55]
for item in l:
    if str(item).isnumeric() and item > 6:
        print(item)
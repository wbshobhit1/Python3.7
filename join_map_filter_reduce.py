#################### JOIN #########################################
###################################################################


print("***************")
print("Join Output")
print("***************")
ipl_teams = ["Mi", "Csk", "Kkr", "Srh", "Rcb", "Dc", "Punjab"]

a = " have there home ground , ".join(ipl_teams)
print(a, " have there home ground")
print("***************")

#################### MAP ##########################################
###################################################################

print("Map Output")
print("***************")
num = ["5", "3", "2", "1", "0"]

# for i in range(len(num)):
#     num[i] = int(num[i])

num = list(map(int, num))

num[4] = num[4] + 1
print(num[4], ", First trophy")

# def sq(a):
#     return a*a

numbers = [4, 8, 7, 6, 16]
square = list(map(lambda x: x*x, numbers))
print(square)

def square (a):
    return a*a
def cube (a):
    return a*a*a

fun = [square, cube]
for i in range(5):
    var = list(map(lambda x: x(i), fun))
    print(var)
print("***************")

#################### FILTER #######################################
###################################################################

print("Filter Output")
print("***************")
def greater_than_5 (a):
    return a > 5

data = [8, 9, 2, 0, 10]
utility = list(filter(greater_than_5, data))
print(utility)
print("***************")

#################### REDUCE #######################################
###################################################################

from functools import reduce
print("Filter Output")
print("***************")
list1 = [1, 4, 8, 7, 6]
# num1 = 0
# for i in range(len(list1)):
#     num1 = num1 + list1[i]
# print(num1)

sum_of_list = reduce(lambda x, y: x+y, list1)
print(sum_of_list)

product_of_list = reduce(lambda x, y: x*y, list1)
print(product_of_list)

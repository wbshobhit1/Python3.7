# f = open("practice.txt","rt")
#
# # readlines function help to read the line of text file in list
#
# # print(f.readlines())
#
# # read lines function use
#
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# print(f.readline())
# f.seek(14)
# print(f.readline())
#
# # content = f.read()
#
# # character by character printing
#
# # for line in content:
# #     print(line)
#
# # line by line printing
#
# # for line in f:
# #     print(line, end="")
#
# # content = f.read(3000)
# # print("1.", content)
# #
# # content = f.read(3)
# # print("2.", content)
# f.close()


#with blocks

with open("practice.txt") as f:
    a = f.readlines()
    print(a)

f = open("practice.txt")
content = f.read()
print(content)
f.close()
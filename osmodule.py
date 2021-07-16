import os

# print(dir(os))
print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
#
# # This will throw error as our current file directory is not where the water.txt is we have changed it to C.
# f = open("water.txt", "r")
print(os.listdir())
print(os.listdir("C://Program Files"))

# os.mkdir("this")
# os.rmdir("this")
# os.makedirs("these/that")
# os.rmdir("these/that")
# os.rmdir("these")
# os.rename("water.txt", "panni.txt")
print(os.environ.get('Path'))
print(os.path.join("C://", "practice.txt"))
print(os.path.exists("C://Program Files"))
print(os.path.isfile("C://Program Files"))
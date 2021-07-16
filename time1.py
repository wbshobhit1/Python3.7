import time
# intial = time.time()
# print(intial)
# i = 0
# while i < 45:
#     print("We can and We will")
#     # time.sleep(2)
#     i = i + 1
# print(f"Time taken to finish this loop is {time.time() - intial} seconds\n")
#
# intial_1 = time.time()
# print(intial_1)
# for i in range(45):
#     print("We can and We will")
#     time.sleep(2)
# print(f"Time taken to finish this loop is {time.time() - intial_1} seconds\n")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)

print(time.time())
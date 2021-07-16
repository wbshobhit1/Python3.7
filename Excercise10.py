import pickle
import requests


r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
text = r.text
print(type(text))
file = "irisdata.txt"
# with open(file, 'a') as f:
#     f.write(text+"\n")

with open(file, 'r') as f:
    content = f.read()

# print(content)
list_of_list = content.split("\n")
list_of_list2 = [item.split(",") for item in list_of_list if len(item) != 0]

# print(list_of_list)
# print(list_of_list2)

# Pickling a Python object

# iris_pickle_file = "irisdata.pkl"
# fileobj = open(iris_pickle_file, 'wb')
# pickle.dump(list_of_list2, fileobj)
# fileobj.close()

# UnPickling a Python object

iris_pickle_file = "irisdata.pkl"
fileobj = open(iris_pickle_file, 'rb')
read_list = pickle.load(fileobj)
fileobj.close()
print(read_list)
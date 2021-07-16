import pickle

# euro2021 =["Austria", "Belgium", "Croatia", "Czech Republic", "Denmark", "England", "Finland", "France", "Germany",
#            "Italy", "Netherlands","Poland", "Portugal", "Russia", "Spain", "Sweden", "Switzerland", "Turkey",
#            "Ukraine", "Wales"]
# # Pickling a Python object
# file = "myteams.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(euro2021, fileobj)
# fileobj.close()

# UnPickling The python object
file = "myteams.pkl"
fileobjt = open(file, 'rb')
euroteams = pickle.load(fileobjt)
print(euroteams)
print(type(euroteams))

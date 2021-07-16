mystr = "aur Bhaiya Kaise Ho Sab Bhadihya"
"""""
print(mystr[:32])
print(len(mystr))
print(mystr[::2])
print(mystr[::])
print(mystr[:7:2])
print(mystr[4::2])
print(mystr[-8:-5])
print(mystr[::-1])

"""
# functions in strings

print(mystr.isalpha())
print(mystr.isalnum())
print(mystr.islower())
print(mystr.istitle())
print(mystr.endswith("bhadhiya"))
print(mystr.endswith("Bhadihya"))
print(mystr.count("a"))
farzi = mystr.capitalize()
print(farzi)
print(mystr.find("Sab"))
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("Bhadihya" , "changa"))
print(mystr.format("Sab"))



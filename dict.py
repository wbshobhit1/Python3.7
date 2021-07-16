"""""
menu = {"chicken rara": 300, "chicken lahori": 320, "chicken tikkka" :280, "panner lababdaar": 250, "garlic naan": 45
        , "drinks": {"pepsi": 20, "sprite": 20, "mazza": 25}}
print(menu["drinks"]["mazza"])
print(menu["garlic naan"])
print(menu["chicken rara"])
print(menu["chicken lahori"])
fav_menu = menu.copy()
fav_menu["chicken biryani"]= 240
fav_menu.update({"aalo partha": 140})

# here line 8 and line 9 code ka mtlb is same ,chahe wo karo ya ye

del fav_menu["drinks"]["pepsi"]
fav_menu["drinks"]["coke"]= 20
print(fav_menu)
print(menu.keys())
print(fav_menu.keys())
print(menu.items())
print(fav_menu.items())
"""

# EXCERCISE 1

words_dict={"mutable": "that can be changed", "immutable": "that cannot be changed", "absurd": "ridiculously unreasonable",
            "stuborn": "persistent", "shred": "finish", "inevitable": "cannot be finished", }
print("Enter the word for the meaning")
y=input()
print(words_dict.get(y))
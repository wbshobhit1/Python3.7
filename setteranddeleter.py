class PlayingXI:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"The email is {fname}.{lname}@indiancricketteam"

    def explain(self):
        return f"This opener is {self.fname} {self.lname}"

    @property #This is a decorator  which allows us to remove function type calling
    def email(self):
        if self.fname is None or self.lname is None:
            return f"Email is not that for our Openers, Set with the help of setter"
        return f"The email is {self.fname}.{self.lname}@indiancricketteam"

    @email.setter # Setters are a great way of performing encapsulation
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter # Deleter is used to delete the values passed as a parameter before.
    def email(self):
        self.fname = None
        self.lname = None


opener1 = PlayingXI("Rohit", "Sharma")
opener2 = PlayingXI("Shikar", "Dhawan")
print(opener1.explain())
print(opener1.email)
opener1.fname = "Lokesh"
opener1.lname = "Rahul"
print(opener1.email)
opener2.email = "prithivi.shaw@indiancricketteam"
print(opener2.fname)
print(opener2.lname)
print(opener2.email)

del opener1.email
print(opener1.email)

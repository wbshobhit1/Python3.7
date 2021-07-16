"""
#Super and Overloading, Using Single inheritance...........

"""


class A:
    classvar1 = "Hey i am in class A variable "

    def __init__(self):
        self.var1 = "Hey this is class A constructor"
        self.classvar1 = "Hey this is Instance Variable of A"
        self.finish = "I want this class to finish"

class B(A):
    classvar1 = "Hey i am in class B variable "

    # classvar2 = 'Hey i am in class B variable'

    def __init__(self):
        # super().__init__()
        self.var1 = "Hey this is class B constructor"
        self.classvar1 = "Hey this is Instance Variable of B"
        super().__init__()


a = A()
b = B()
# if we want to run child class first we initialize super at the start of the method.
#print(b.var1, b.classvar1, b.finish)

# if we want to run child class first we initialize super at the end of the method.
print(b.var1, b.classvar1, b.finish)

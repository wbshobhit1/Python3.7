# def funct1():
#     print("kkr beat punjab by 5 wickets")
#
#
# funct2 = funct1()
# del funct1
# funct2

# def exceutor (func):
#     func("this")
#
# exceutor(print)(



def dec1(func1):
    def nowexecute():
        print("Executing the function")
        func1()
        print("Executed")
    return nowexecute

@dec1
def ipl_news():
    print("kkr beat punjab by 5 wickets")

ipl_news()
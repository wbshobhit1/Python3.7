# Health managment System Type 2

def getdate():
    import datetime
    return datetime.datetime.now()

def log(k):
    if k == 1:
        c = int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            value = input("Entry\n")
            with open("harry--diet.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
            print("Entered succesfully")
        elif c is 2:
            value = input("Entry\n")
            with open("harry--excerise.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + value + "\n")
            print("Entered succesfully")
    elif k == 2:
        c = int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            value = input("Entry\n")
            with open("rohan--diet.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
            print("Entered succesfully")
        elif c is 2:
            value = input("Entry\n")
            with open("rohan--excerise.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + value + "\n")
            print("Entered succesfully")
    elif k == 3:
        c = int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            value = input("Entry\n")
            with open("hammad--diet.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
            print("Entered succesfully")
        elif c is 2:
            value = input("Entry\n")
            with open("hammad--excerise.txt", "a") as f:
                f.write(str([str(getdate())]) + ":" + value + "\n")
            print("Entered succesfully")
    else:
        print("Enter valid entry 1-Harry,2-Rohan,3-Hammad")

def retrive(k):
    if k == 1:
        c= int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            with open("harry--diet.txt") as f:
                for i in f:
                    print(i, end="")
        elif c is 2:
            with open("harry--excercise.txt") as f:
                for i in f:
                    print(i, end="")

    elif k == 2:
        c= int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            with open("rohan--diet.txt") as f:
                content = f.read()
                for i in content:
                    print(i, end="")
                f.close()
        elif c is 2:
            with open("rohan--excercise.txt") as f:
                for i in f:
                    print(i, end="")
                f.close()
    elif k == 3:
        c= int(input("Press 1 for Diet and 2 for Excercise"))
        if c is 1:
            with open("hammad--diet.txt") as f:
                for i in f:
                    print(i, end="")
        elif c is 2:
            with open("hammad--excercise.txt") as f:
                for i in f:
                    print(i, end="")

    else:
        print("Enter valid entry 1-Harry,2-Rohan,3-Hammad")


a= int(input("Press 1 to log the entry and Press 2 to retrive the Data "))
if a is 1:
    print("Press 1 for Harry")
    print("Press 2 for Rohan")
    print("Press 3 for Hammad")
    b = int(input())
    log(b)
elif a is 2:
    print("Press 1 for Harry")
    print("Press 2 for Rohan")
    print("Press 3 for Hammad")
    c = int(input())
    retrive(c)
else:
    print("Enter valid entry 1-Harry,2-Rohan,3-Hammad")


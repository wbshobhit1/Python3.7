# HEALTH MANAGMENT SYSTEM

client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
log_list = {1: "Diet", 2: "Excercise"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:::")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client::", client_list.get(client_name), "\n", end="")

    print("Press 1 for log ")
    print("Press 2 to retrieve")
    opt = int(input())

    if opt is 1:
        for key, value in log_list.items():
            print("Press ", key, "for", value, "\n", end="")
        log_name = int(input())
        print("Selected Job::", log_list.get(log_name), "\n", end="")
        f = open(client_list.get(client_name) + "--" + log_list.get(log_name) + ".txt", "a")
        k = "Y"
        while k is not "N":
            print("Enter", log_list.get(log_name), "\n", end="")
            mytext = input()
            f.write("[" + str(getdate()) + "]:" + mytext + "\n")
            print("Want to Add more press Y else press N \n", end="")
            k = input()
            continue
        f.close()
    elif opt is 2:
        for key, value in log_list.items():
            print("Press ", key, "for", value, "\n", end="")
        log_name = int(input())
        print(client_list.get(client_name) + "--" + log_list.get(log_name) + "Report\n", end="")
        f = open(client_list.get(client_name) + "--" + log_list.get(log_name) + ".txt")
        content = f.read()
        for i in content:
            print(i, end="")
        f.close()
    else:
        print("Invalid input")

except Exception as e:
    print("Worng input OR Empty data set")

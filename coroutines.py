# def searcher():
#     import time
#     book = "this is book of mine, contains everything about cricket"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your Text is present in the book")
#         else:
#             print("Text not [resent in the book")
#
#
# search = searcher()
# print("search started")
# next(search)
# search.send("cricket")
# input("Press any key")
# search.send("about cricket")
# search.close()
# # After closing  the the coroutine we cannot again send the request again as we are using yield as same as Generator.
# # search.send("book")

# Search names from the text file

def name_searcher():
    import time
    f = open("names.txt", "r")
    list1 = f.read()
    time.sleep(4)

    while True:
        name = (yield)
        if name in list1:
            print("Your name is present in the Letter List")
        else:
            print("Name not present in the Letter List")


search = name_searcher()
print("search started")
next(search)
search.send(input("Enter the Name: "))
input("Press any key to terminate")

search.close()
# After closing  the the coroutine we cannot again send the request again as we are using yield as same as Generator.
# search.send("book")



def funargs(normal, *args, **kwargs):
    print(normal)
    print(type(args))
    for i in args:
        print(i)
    print(type(kwargs))
    print("\nDates with Initials")
    print("************************")
    for key, value in kwargs.items():
        print(f"The month {key} belongs to {value} and this his initial")


bday = ["feb", "march", "april", "june", "september", "october"]
normal = "I am normal argument and this is the list of birthdays of guys"
initials = {"feb": "A", "march": "J", "april": "A,S", "june": "S", "september": "Abhi,Sinha", "october": "D"}
funargs(normal, *bday, **initials)

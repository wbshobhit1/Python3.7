from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def New_user(self):
        return 0


class Github(User):
    Sign_in = "Email or username\nPassword "
    Resgister = "Sign up"

    def __init__(self, Email, Username, Mobileno, Password, Dob):
        self.email = Email
        self.user = Username
        self.mobile = Mobileno
        self.password = Password
        self.dob = Dob

    def New_user(self):
        return f"Welcome user {self.user}\nVerify your account by clicking on the link sent on your registered Mobile " \
               f"Number {self.mobile}\nPending...."

class Google(User):
    pass


User1 = Github("abc.gamil.com", "abc", 786555545, "admin12345", ["04-06-1999"])
print(User1.Sign_in)
print(User1.Resgister)
print(User1.New_user())

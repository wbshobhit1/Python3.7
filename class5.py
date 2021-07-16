"""
Static method use if we don't have to use static or class instances then we use static method ,And why we are using in
inside the class because when we want to fix some function for that class we use static without using the instances of
class and object.
"""
class Ipl:
    total_seasons = 13

    def __init__(self, team_name, tittle, captain, win_year):
        self.team_name = team_name
        self.title = tittle
        self.captain = captain
        self.win_year = win_year

    def print_details(self):
        return f"No of title won by {self.team_name} is {self.title} and the captain was {self.captain}, in years {self.win_year}"

    @classmethod
    def season_increase(cls, new_season):
        cls.total_seasons = new_season

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2], params[3])
        return cls(*string.split("-"))

    @staticmethod
    def imp_news(string):
        print("Bio bubble burst In Ipl 2021,Teams like "+string+" were suffering from covid crisis ")
        return "Ipl 2021 is suspended ,can't be played in this absurd situation"
    pass


Mi = Ipl.from_dash("Mumbai Indians-5-Rohit Sharma-[2013, 2015, 2017, 2019, 2020]")

Csk = Ipl.from_dash("Chennai Super Kings-3-Ms Dhoni-[2010, 2011, 2018]")

Kkr = Ipl.from_dash("Kolkata Knight riders-2-Gautam Gambhir-[2012, 2014]")

Srh = Ipl.from_dash("Hydrebad-2-[David Warner,Adam Gilchrist]-[2009, 2016]")

Rr = Ipl.from_dash("Rajasthan Royals-1-Shane warne-[2008]")

# print(Mi.print_details())
# print(Csk.print_details())
# print(Kkr.print_details())
# print(Srh.print_details())
# print(Rr.print_details())
print("Season News", end=" ")
print(+Ipl.total_seasons)

print(Ipl.imp_news("Kkr, Csk, Dc and Srh"))
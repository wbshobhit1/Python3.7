class Ipl:
    total_seasons = 12

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

    pass


Mi = Ipl("Mumbai Indians", 5, "Rohit Sharma", [2013, 2015, 2017, 2019, 2020])

Csk = Ipl("Chennai Super Kings", 3, "Ms Dhoni", [2010, 2011, 2018])

Kkr = Ipl("Kolkata Knight riders", 2, "Gautam Gambhir", [2012, 2014])

Srh = Ipl("Hydrebad", 2, ["David Warner", "Adam Gilchrist"], [2009, 2016])

Rr = Ipl("Rajasthan Royals", 1, "Shane warne", [2008])

print(Mi.print_details())
print(Csk.print_details())
print(Kkr.print_details())
print(Srh.print_details())
print(Rr.print_details())
Mi.total_seasons = 13
print(Mi.total_seasons)
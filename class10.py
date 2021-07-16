class Wtc:

    def __init__(self, played, wins, last_res):
        self.played = played
        self.wins= wins
        self.last_res = last_res

    def printdetailsind(self):
        return f"Wtc final will take place in Southamphon Rose's Bowl stadium having capacity of 25,000 and team \nIndia"\
               f"had played {self.played} matches and wins is {self.wins} , about latest result {self.last_res} ."

    def printdetailsnz(self):
        return f"Wtc final will take place in Southamphon Rose's Bowl stadium having capacity of 25,000 and team \n" \
               f"Newzeland had played {self.played} matches and wins is {self.wins},about latest result {self.last_res}."

    def __truediv__(self):
        return self.wins / self.played

    def __add__(self, other):
        return self.played + other.played

    def __and__(self, other):
        return self.wins & other.wins


Ind = Wtc(19, 4, "Lost by 60 runs in 2018")
Nz = Wtc(16, 3, "Never played here")
print(Ind.printdetailsind())
print("win percentage is ", Ind.wins/Ind.played*100, "%")
print(Nz.printdetailsnz())
print("win percentage is ", Nz.wins/Nz.played*100, "%")

print(f"totals matches played by both team as a whole is {Ind + Nz}")
print(Ind & Nz)
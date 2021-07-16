class Ipl:
    pass


Mi = Ipl()
Csk = Ipl()

Mi.tittle = 5
Csk.tittle = 3
Mi.captain = "Rohit Sharma"
Csk.captain = "Ms Dhoni"
Mi.winyear = [2013, 2015, 2017, 2019, 2020]
Csk.winyear = [2010, 2011, 2018]

print("Max Ipl winning captains are", Mi.captain, "&", Csk.captain)
print("Number ipls won by mumbai and chennai respectively ", Mi.tittle, "&", Csk.tittle)
print("IPl year win list for  mumbai and chennai respectively ", Mi.winyear, "&", Csk.winyear)
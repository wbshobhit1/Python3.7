import sklearn as sk

print(sk.__version__)

from sklearn.ensemble import RandomForestClassifier

print(RandomForestClassifier())

import  file2

file2.iplnews("Mumbai lost the match aginst Dc by 6 wickets")
p = file2.resultbet(40, 12)
print("Total loss is", p)
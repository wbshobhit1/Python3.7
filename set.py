s = set()
"""""
print(type(s))
l= [1, 2, 3, 4]
s_of_list = set(l)
print(s_of_list)
print(type(s_of_list))

"""
s.add(1)
#s.add(1)
s.add(2)
s1 =s.union({1, 2, 3})
s2 = s.intersection({1, 2, 3})
print(s, s1)
print(s, s2)
s3 = ({4, 5, 1})
print(s.isdisjoint(s3))
print(s.difference(s3))
print(s.symmetric_difference(s3))
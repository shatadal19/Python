s = {2,4,2,6}
s1 = {1,4,5,7,9}

# print(s.union(s1))
print(s.intersection(s1))
print(s.symmetric_difference(s1))
print(s.isdisjoint(s1))
print(s.issuperset(s1))
print(s.issubset(s1))
s.add(10)
print(s)
s.remove(10)
print(s)
# del s
# print(s)


print(s,s1)
s.update(s1)
print(s)


# print(s)
# info = {'car', 19,False,5.9}
# print(info)
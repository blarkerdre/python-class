#Create an empty set
s = set()

#add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

#no duplicate number in set
s.add(3)
print(s)

#removing a number in a set
s.remove(2)
print(s)

print("the set has ", len(s), "elements")
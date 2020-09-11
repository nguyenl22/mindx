# q1
a=['ST','BĐ','BTL','CG','ĐĐ','HBT']
b=[150300,247100,333300,266800,420900,318000]
print(a)
print(b)
# q2
print('Index of district with the highest population is:',b.index(max(b)))
print('Index of district with the lowest population is:',b.index(min(b)))
# q3
c=int(b.index(max(b)))
print('The most populated district is:',a[c])
d=int(b.index(min(b)))
print('The least populated dítrict is:',a[d])




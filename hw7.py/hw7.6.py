# q1
a=['ST','BĐ','BTL','CG','ĐĐ','HBT']
b=[150300,247100,333300,266800,420900,318000]
c=[11743,9224,4335,1204,996,1009]
d=[]
for item in b:
    e=item%c[int(b.index(item))]
    d.append(e)
print('List of districts population densities:',d)
# q2
average=sum(d)/len(a)
print('Average population density is:', average)

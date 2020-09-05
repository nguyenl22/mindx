print("list intro")
list=['a','b']
# 1 list co the chua dif kinds of variables
# list modifications: create (list.append()), read (list[0]), update (list[index]=replacement), delete (list.remove(value), list.pop(index))
# create
list.append('c')
print(list[0])
# list[-1]=c (index no.-1 is the last item)
# meaning: print item index no.0 in list
# read
print(list)
for i in range (3):
    print(list[i])
for i in range(len(list)):
    print(list[i])
for item in list:
    print(item)
# in tung item theo index
for index,item in enumerate(list):
    print(index,item)
# update
list[0]='d'
print(list)
# delete
list.remove('c')
print(list)
list.pop(0)
print(list)



    
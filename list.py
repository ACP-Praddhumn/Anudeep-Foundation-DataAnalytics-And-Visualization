# create a list of 20 elements and display elements using forward index in reverse order

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list1 = [i for i in range(1,21)]

for x in range(len(list)-1, -1, -1):
    print(list[x], end=' ')

print("--------------------------------------------------------------------")

for x in range(-1, -len(list1)-1, -1):
    print(list1[x], end=' ')

print("--------------------------------------------------------------------")

for x in range(len(list)):
    print(list[len(list)-x-1], end=' ')

firstList = [20,45,6,8]
firstList.extend([4,7,2])
print(firstList)
del firstList[1:3:1]
print(firstList)
del firstList[2]
print(firstList)
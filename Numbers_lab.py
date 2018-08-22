myList = [2, 3, 50, 40, 7, 25, 45, 87, 90, 10]
OrganizedList = []

while myList:
    minimum = myList[0]  
    for x in myList: 
        if x < minimum:
            minimum = x
    OrganizedList.append(minimum)
    myList.remove(minimum)   

print(OrganizedList)
print(OrganizedList[::-1])
print('wow')
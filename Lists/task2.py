# take list from user append all element in list and remove duplicate element in the list. 
#          input : [1,2,3,4,4,5,5,6,7,8,9,9,10]
#          output : [1,2,3,4,5,6,7,8,9,10]


l1 = []
num = int(input("Enter number of elements you want to add in list: "))
for i in range(num):
    element = int(input("Enter element: "))
    if element not in l1:
        l1.append(element)
print(l1)
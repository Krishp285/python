# take list from user append all element in list and print pelindorme num in list 
 
#          input : [121 , 131 , 123 ,145 , 789 ]
#          output :  [121,131]

l1 = []
palindrome = []
num = int(input("Enter number of elements you want to add in list: "))
for i in range(num):
    element = int(input("Enter element: "))
    l1.append(element)
    if str(element) == str(element)[::-1]:
        palindrome.append(element)

print(palindrome)

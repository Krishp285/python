# strong  number  :   import  math   == > factorial() 
"""
145 : 

each digit  :  factorial  : 
1 fact = 1   4 fact =24  5 fact =120 

sum = 1 + 24 +120 =145   == > strong number  :   nested  loop  
"""

"""n=int(input("enter the  number  : ")) # 145 
digit = len(str(n))  # 3 
sum =0 
temp =n    # temp =145 
for i in range(digit):   #  2    
    r=  temp % 10      # r = 1 %10 =1 
    fact =1 
    for j in range(1,r+1) : # 1,2 
        fact =fact *j      # fact =1  
    sum =sum +fact   # sum =144 +1 =145
    temp = temp //10 # 1 //10 =0  
if sum ==n :   # 145 == 145 
    print(n,"is a strong number")
"""

# nested loop  : prime  amg twin  pelindorme 

"""
start =int(input("enter the start number  : "))
end =int(input("enter the end number  : "))

for  i in range(start,end +1):   # 100 -100000 
    digit = len(str(i))  #  3 
    temp =i 
    sum =0 
    for j in range(digit):   # 3 
        r = temp %10  
        sum =sum +pow(r,digit)
        temp  = temp //10
    if sum ==i : 
        print(i,end=" ")
"""
# hw : prime , perfect ,twin  , strong in range ,   nested loop  

# next :  pattern  

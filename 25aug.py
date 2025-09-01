# perfect number in range  : 

"""
6 = 1,2,3,6   ==> sum  = 1+2+3 =6    perfect 
28 =1,2,4,7,14,28 ==>sum = 1+2+4+7+14 =28  ==> perfect  

"""

"""
start = int(input("enter the start number  : "))
end= int(input("enter the end number  : "))

for i in range(start,end+1):   # 6 -10000
    sum =0   # 0 
    for j in range(1,i): # 1,6
        if i % j==0 : 
            sum =sum + j 
    if sum ==i : 
        print(i,end=" ")
"""

# pattern  : 

"""
1.          2.          3.          4.          5.          6. 
 
* * * * *   *          * * * * *    1           5 4 3 2 1   1 2 3 4 5 
* * * * *   * *        * * * *      1 2         5 4 3 2     2 3 4 5
* * * * *   * * *      * * *        1 2 3       5 4 3       3 4 5
* * * * *   * * * *    * *          1 2 3 4     5 4         4 5
* * * * *   * * * * *  *            1 2 3 4 5   5           5
"""
# 1: 
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
#2. 
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#3 . 
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

"""
7.         8.           9.          10. 
  
* * * * *   * * * * *         *      * 
  * * * *    * * * *        * *     * *
    * * *     * * *       * * *    * * * 
      * *      * *      * * * *   * * * *
        *       *     * * * * *  * * * * *

"""

#7. 

"""
for i in range(1,6):  # 2 ,6 
    for k in range(1,i):  # 1,2
        print(" ",end=" ")
    for j in range(5,i-1,-1):  # 5 ,1
        print("*",end=" ")    #  * * * * * 
    print()                   #    * * * * 
"""
#8 :
"""
for i in range(1,6):  # 2 ,6 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1):  # 5 ,1
        print("*",end=" ")    #  * * * * * 
    print()                   #    * * * * 
"""
# 9 : 

"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#10. 

"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""

# 11. full pyramid: 

"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):  # 2 ,6 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1):  # 5 ,1
        print("*",end=" ")    #  * * * * * 
    print()
"""

"""
# 12.       13 .        14.        15.          16.

* * * * *   *           * * * * *       *        * * * * *
*       *   * *         *     *        * *        *     *
*       *   *   *       *   *         *   *        *   *
*       *   *     *     * *          *     *        * *
* * * * *   * * * * *   *           * * * * *        *
"""
#12. 
"""
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""
#13. 
for i in range(1,6):
    for j in range(1,i+1):
        if(i==1 or i==5 or j==1 or i==j):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

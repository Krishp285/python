for i in range(5,0,-1):
    for j in range(i):
        if(i==1 or i==5 or j==1 or j == i-1):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

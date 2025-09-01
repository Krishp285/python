# Pattern 1 : 
    # *****
    # *****
    # *****
    # *****
    # *****

for i in range(5):
    print("*" * 5)

#  Pattern 2 
    # *
    # **
    # ***
    # ****
    # *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Pattern 3
    # *****
    # ****
    # ***
    # **
    # *

for i in range(5, 0, -1):
    print("*" * i)

# Pattern 4
    # 1
    # 12
    # 123
    # 1234
    # 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Pattern 5
    # 54321
    # 5432
    # 543
    # 54
    # 5

    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(6 - j, end="")
        print()

# Pattern 6
    # 12345
    # 2345
    # 345
    # 45
    # 5

for i in range(1,6):
    for j in range(i,6):
        print(j,end="")
    print()

# Pattern 7
    # *****
    #  ****
    #   ***
    #    **
    #     *

for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * i)

# Pattern 8 
    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *

for i in range(5, 0, -1):
    print(" " * (5-i), end="")
    for j in range(i):
        print("* ", end="")
    print()

#Pattern 9 
    #        *
    #       **
    #      ***
    #     ****
    #    *****

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Pattern 10
    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *

for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print("* ", end="")
    print()

# Pattern 11
    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(2,6):  
    for k in range(1,i): 
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()

# Pattern 12
    # *****
    # *   *
    # *   *
    # *   *
    # *****

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Pattern 13
    # *
    # * *
    # *   *
    # *     *
    # * * * * *

for i in range(5):
    for j in range(5):
        if i == j or j == 0 or i == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Pattern 14
    # *****
    # *  *
    # * *
    # **
    # *  

for i in range(5,0,-1):
    for j in range(i):
        if(i==0 or i==5 or j==0 or j == i-1):
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()


# Pattern 15
    #      *
    #     * *
    #    *   *
    #   *     *
    #  * * * * *
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        if i == 5 or j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# Pattern 16
    #* * * * *
    # *     *
    #  *   *
    #   * *
    #    *

for i in range(5, 0, -1):
    print(" " * (5-i), end="")
    for j in range(i):
        if i == 0 or j == 0 or i == 5 or j == i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
def prime(l):
    for i in l:
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            nl.append(i)
    

l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nl = []
print(prime(l)) # [2, 3, 5, 7, 11, 13, 17, 19] 
print(nl)
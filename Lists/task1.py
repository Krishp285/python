l1=[1,2,3,4,5,6,7,80,900,12.56,100,100]
even = []
odd = []
for i in l1 :
    if i%2==0 :
        even.append(i)
    else :
        odd.append(i)

print("even =", even)
print("odd =", odd)

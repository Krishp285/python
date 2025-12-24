l1 = [1, 2, 3, 4, 5]
odd = list(filter(lambda x : x%2 != 0 ,l1))
print(odd)
even = list(filter(lambda x : x%2 == 0 ,l1))
print(even)

l2 = [1, 2, 3, 4, 5]
ans = list(map(lambda x : x*x ,l2))
print(ans)



 
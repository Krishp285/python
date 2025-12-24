# Sort a list of lists based on the second element of each sublist
l = [[10,20],[20,10],[30,5],[40,3],[50,7]]

def sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i][1] > l[j][1]:
                l[i], l[j] = l[j], l[i]
    return l
print(sort(l)) 

def sort2(l):
    return l[1]
l1 = [[10,20],[20,10],[30,5],[40,3],[50,7]]
print(sorted(l1, key = sort2))

# using lambda function
l = [[10,20],[20,10],[30,5],[40,3],[50,7]]
l.sort(key = lambda x: x[1]) # sorted(l,key = lambda x: x[1])
print(l) 


# Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
l.sort(key = lambda x: x[1])
print(l)
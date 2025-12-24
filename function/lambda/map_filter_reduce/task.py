# Find all palindromic numbers in the given list using lambda and filter or map function.
input = [1221,"php",12321,"java",1234321,"python"]

ans = list(filter(lambda x : str(x) == str(x)[::-1],input))
print(ans)


# Reverse all the strings in the given list using lambda and map function.

l = ['Red', 'Green', 'Blue', 'White', 'Black']

reverse = list(map(lambda x : x[::-1],l))
print(reverse)


#Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.

# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height> 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

new_dict = dict(filter(lambda x : x[1][0] >= 6 and x[1][1] >= 70, students.items()))
print(new_dict)
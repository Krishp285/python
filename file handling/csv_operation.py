import csv 

with open('students.csv','w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 14, 'A'])
    writer.writerow(['Bob', 15, 'B'])
    writer.writerow(['Charlie', 13, 'A+'])

with open('students.csv','r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('students.csv','w',newline='')as file:
    fieldnames = ['Name', 'Age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'David', 'Age': 16, 'city': 'New York'})
    writer.writerow({'Name': 'Eva', 'Age': 14, 'city': 'Los Angeles'})
    writer.writerow({'Name': 'Frank', 'Age': 15, 'city': 'Chicago'})

with open('students.csv','r')as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

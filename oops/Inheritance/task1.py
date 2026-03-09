# Implement the following hierarchy . The Book function has name, n (number of authors), authors (list of authors), 
# publisher, ISBN, and year as its data members and the derived class has course as its data member. The derived class 
# method overrides (extends) the methods of the base
# class.

class Book:
    def __init__(self , name , n , authors , publisher , ISBN , year):
        self.name = name
        self.n = n
        self.authors = authors
        self.publisher = publisher
        self.ISBN = ISBN
        self.year = year

    def display(self):
        print(f"Book Name: {self.name}")
        print(f"Number of Authors: {self.n}")
        print(f"Authors: {', '.join(self.authors)}")
        print(f"Publisher: {self.publisher}")
        print(f"ISBN: {self.ISBN}")
        print(f"Year: {self.year}")

class Course(Book):
    def __init__(self, name, n, authors, publisher, ISBN, year, course):
        super().__init__(name, n, authors, publisher, ISBN, year)
        self.course = course

    def display(self):
        super().display()
        print(f"Course: {self.course}")

book = Course("Introduction to Programming", 2, ["Alice", "Bob"], "TechBooks Publishing", "123-4567890123", 2021, "CS101")
book.display()
C = Course("Data Structures", 1, ["Charlie"], "EduBooks Publishing", "987-6543210987", 2020, "CS102")
C.display()
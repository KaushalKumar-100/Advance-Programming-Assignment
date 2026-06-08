from abc import ABC, abstractmethod

# Abstract Base Class
class LibraryItem(ABC):
    item_count = 0   # static/class variable (extra feature)

    def __init__(self, title, year=0):  # default argument used
        self.title = title
        self.year = year
        LibraryItem.item_count += 1

    @abstractmethod
    def displayInfo(self):
        pass


# Subclass: Bookgit 
class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def displayInfo(self):   
        print(f" Book: {self.title}, Author: {self.author}, Year: {self.year}")


# Subclass: DVD
class DVD(LibraryItem):
    def __init__(self, title, year, duration, genre):
        super().__init__(title, year)
        self.duration = duration
        self.genre = genre

    def displayInfo(self):   # method overriding
        print(f" DVD: {self.title}, Genre: {self.genre}, Duration: {self.duration} mins, Year: {self.year}")


#  Polymorphism using collection of LibraryItem objects
items = [
    Book("The Alchemist", 1988, "Paulo Coelho"),
    DVD("Inception", 2010, 148, "Sci-Fi"),
    Book("Python Basics", 2022, "John Doe")
]

for item in items:
    item.displayInfo()   # polymorphism in action


# Static counter usage
print("\nTotal Library Items:", LibraryItem.item_count)
        
    
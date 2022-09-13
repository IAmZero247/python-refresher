from typing import List
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name, self.price !r}"

    @property
    def bookdetail(self):
        return f"{self.name, self.price !r}"


class Order:

    def __init__(self, *books : List[Book]):
        self.books = books;

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

    def printbooks(self):
        # to get details of books
        list1 = list(map(lambda i: i.bookdetail, self.books))
        return list1




book1 = Book("Harry Potter" , 200)
print(book1)
book2 = Book("Python 101", 100)
print(book2)

order = Order(book1, book2)
print(order)
print(type(order.books))
print(order.printbooks())

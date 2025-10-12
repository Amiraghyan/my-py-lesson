class Book():
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
    
    def description(self) :
        return {"title": self.title, "author": self.author}

book1 = Book("Հովհաննես Թումանյան", "Չախչախ թագավորը")
book2 = Book("Ավետիք Իսահակյան", "Նուկիմ քաղաքի խելոքները")

print(book1.description())
print(book2.description())


print(book1.description()["title"], book1.description()["author"], sep = " - ")
print(book2.description()["title"], book2.description()["author"], sep = " - ")
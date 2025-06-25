class Book:
 
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out
        
    
class Library(Book):
    
    def __init__(self,title, books):
        
        super().__init__(title)
        self._books = books
        
    def add_book():
        Book = {}
        return Book
    
    def check_out_book(title):
        pass
    
    def return_book(title):
        pass
    
    def list_available_books(title):
        pass
        
        
class Book:
    
    def __init__(self, title, author, is_checked_out):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
        
    
class Library(Book):
    
    def __init__(self,title, is_checked_out):
        
        super().__init__(title, is_checked_out)
        
        
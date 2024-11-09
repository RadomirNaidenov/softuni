from project.user import User


class Library:

    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for key, value in self.books_available.items():
            if book_name in value:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                self.rented_books[user.username] = {book_name: days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
        for book in user.books:
            if book == book_name:
                for guy, value in self.rented_books.items():
                    if guy == user.username:
                        days_left = self.rented_books[guy][book]
                        return f'The book "{book_name}" is already rented and will be available in {days_left} days!'

    def return_book(self, author: str, book_name:str, user: User) -> str:
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        if author in self.books_available:
            self.books_available[author].append(book_name)
        if user.username in self.rented_books:
            if book_name in self.rented_books[user.username]:
                self.rented_books[user.username].pop(book_name)













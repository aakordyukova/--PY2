from typing import Optional
from pydantic import BaseModel

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    id: int
    name: str
    pages: int

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id={self.id}, name={self.name!r}, pages={self.pages})'


class Library(BaseModel):
    books: Optional[list]

    def get_next_book_id(self):
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку."""
        if self.books is None:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int):
        """Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса."""
        id_index = -1
        for book in self.books:
            if book.id == id_:
                id_index = self.books.index(book)
        if id_index == -1:
            raise ValueError('Книги с запрашиваемым id не существует')
        else:
            return id_index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

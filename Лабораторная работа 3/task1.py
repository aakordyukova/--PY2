class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """Дочерний класс Бумажные книги"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    # Метод __str__ унаследован

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Число страниц должно быть целым числом (int)!")
        elif new_pages <= 0:
            raise ValueError("Число страниц должно быть положительным числом!")
        self._pages = new_pages


class AudioBook(Book):
    """ Дочерний класс Аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

    # Метод __str__ унаследован

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть целым числом (int)!")
        elif new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом!")
        self._duration = new_duration

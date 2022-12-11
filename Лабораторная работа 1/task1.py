import doctest


class LightsGarland:
    def __init__(self, color: str, length: int, number_of_modes: int, current_mode_number: int):
        """
                Создание и подготовка к работе объекта "Гирлянда"

                :param color: Цвет огоньков
                :param length: Длина гирлянды в метрах
                :param number_of_modes: Количество режимов работы
                :param current_mode_number: Текущий режим работы гирлянды

                Пример:
                >>> garland = LightsGarland('multicolored', 3, 5)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет гирлянды должен быть описан переменной типа str")
        self.color = color

        if not isinstance(length, (int)):
            raise TypeError("Длина гирлянды должна быть задана в метрах переменной типа int или float")
        if length <= 0:
            raise ValueError("Длина гирлянды должна быть положительным числом")
        self.length = length

        if not isinstance(number_of_modes, int):
            raise TypeError("Количество режимов работы должно быть описано переменной типа int")
        if number_of_modes <= 0:
            raise ValueError("Количество режимов работы должно быть положительным числом")
        self.number_of_modes = number_of_modes

        if not isinstance(current_mode_number, int):
            raise TypeError("Номер режима работы должен быть описан переменной типа int")
        if current_mode_number <= 0 or current_mode_number > number_of_modes:
            raise ValueError(f"Номер режима работы должен быть положительным числом, лежащим в интервале [0; {number_of_modes}]")
        self.current_mode_number = current_mode_number

    def lights_on_off(self) -> None:
        """ Включение и выключение гирлянды. """
        ...

    def change_mode(self, mode_number: int) -> None:
        """
        Переключение гирлянды на заданный режим работы.

        :param mode_number: Номер режима работы, на который нужно переключить гирлянду

        :raise Exception: Если гирлянда выключена, то нельзя изменить режим её работы

        Пример:
        >>> garland = LightsGarland
        >>> garland.change_mode(2) # переключает гирлянду на второй режим работы
        """
        if not isinstance(mode_number, int):
            raise TypeError("Номер задаваемого режима работы должен быть описан переменной типа int")
        if mode_number <= 0 or mode_number > self.number_of_modes:
            raise ValueError(f"Номер желанного режима работы должен быть положительным числом, лежащим в интервале [0; {self.number_of_modes}]")
        ...

class LinearFunction:
    """ Класс описывает линейные функции вида y = ax + b. """
    def __init__(self, parameter_a: float, parameter_b: float):
        """
        Инициализация экземпляра класса.

        :param parameter_a: Угловой коэффициент
        :param parameter_b: Свободный коэффициент

        Пример:
        >>> line1 = LinearFunction(1.0, 3.5)
        """
        if not isinstance(parameter_a, float):
            raise TypeError("Угловой коэффициент a должен быть задан переменной типа float")
        self.parameter_a = parameter_a

        if not isinstance(parameter_b, float):
            raise TypeError("Свободный коэффициент b должен быть задан переменной типа float")
        self.parameter_b = parameter_b

    def find_intersection_point_ox(self) -> tuple:
        """
        Нахождение точки пересечения с осью OX.

        :return: Кортеж с координатами точки пересечения с осью OX
        """
        ...

    def check_point(self, x: float, y: float) -> bool:
        """
        Проверяет, принадлежит ли заданная точка, прямой.

        :param x: Абсцисса заданной точки
        :param y: Ордината заданной точки
        :return: Принадлежит ли заданная точка прямой

        Пример:
        >>> line1 = LinearFunction(0.5, 3.5)
        >>> line1.check_point(1.0, 2.3)
        """
        if not isinstance(x, float):
            raise TypeError("Абсцисса точки (х) должна быть задана переменной типа float")
        if not isinstance(y, float):
            raise TypeError("Ордината точки (y) должна быть задана переменной типа float")
        ...

class MusicCompactDisk:
    """ Класс описывает музыкальные компакт-диски."""
    def __init__(self, cd_name: str, artist_name: str, number_of_songs: int):
        """
        Инициализация экземпляра класса.

        :param cd_name: Название диска
        :param artist_name: Исполнитель
        :param number_of_songs: Количество песен
        """
        if not isinstance(cd_name, str):
            raise TypeError("Название диска должно быть описано переменной типа str")
        self.cd_name = cd_name

        if not isinstance(artist_name, str):
            raise TypeError("Имя исполнителя должно быть описано переменной типа str")
        self.artist_name = artist_name

        if not isinstance(number_of_songs, int):
            raise TypeError("Количество песен должно быть описано переменной типа int")
        if number_of_songs <= 0:
            raise ValueError("Количество песен должно быть положительным числом")
        self.number_of_songs = number_of_songs

    def is_song_in(self, song_name: str) -> bool:
        """
        Определяет, есть ли на диске песня с заданным названием.

        :param song_name: Название искомой песни
        :return: Есть ли искомая песня на диске

        Пример:
        >>> cd1 = MusicCompactDisk("HEAL", "The Rose", 10)
        >>> cd1.is_song_in('Shift')
        """
        if not isinstance(song_name, str):
            raise TypeError("Название песни должно быть описано переменной типа str")
        ...

    def next_song(self) -> None:
        """ Переключение на следующую песню. С последней песни переключение идёт на первую. """
        ...


if __name__ == "__main__":
    doctest.testmod()

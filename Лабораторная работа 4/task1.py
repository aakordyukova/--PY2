class MedTest:
    """ Базовый класс Медицинские анализы.

     Инициализация объекта Медицинский анализ
        :param test: Название анализа
        :param patient: ФИО пациента
        Пример:
        >>> some_test = MedTest("Анализ мочи", "Иванов Иван Иванович")
        >>> print(some_test)
        Исследование: Анализ мочи. Пациент: Иванов Иван Иванович.
        >>> print(repr(some_test))
        MedTest(test='Анализ мочи', patient='Иванов Иван Иванович')
     """
    def __init__(self, test: str, patient: str):
        self._test = test
        self._patient = patient

    def __str__(self):
        return f"Исследование: {self._test}. Пациент: {self._patient}."

    def __repr__(self):
        return f"{self.__class__.__name__}(test={self._test!r}, patient={self._patient!r})"

    @property
    def test(self):
        """Возвращает название анализа/исследования"""
        return self._test

    @test.setter
    def test(self, new_test: str) -> None:
        """Устанавливает название анализа/исследования."""
        if not isinstance(new_test, str):
            raise TypeError("Название анализа/исследования должно быть типа str")

    @property
    def patient(self):
        """Возвращает ФИО пациента"""
        return self._patient

    @patient.setter
    def patient(self, new_patient: str) -> None:
        """Устанавливает ФИО пациента."""
        if not isinstance(new_patient, str):
            raise TypeError("ФИО пациента должно быть типа str")

    @staticmethod
    def warning() -> str:
        """ Метод, позволяющий вывести информацию о результатах для пациента."""
        return "Интерпретацию полученных результатов проводит врач"

    @staticmethod
    def preparation_info() -> str:
        """ Метод, выводящий информацию о необходимой подготовке к исследованию"""
        return "Подготовки не требуется"


class BloodTest(MedTest):
    """Дочерний класс Анализ крови

    Инициализация объекта Анализ крови
        :param test: Название анализа
        :param patient: ФИО пациента
        :param sample_code: Код пробирки
        :param indicator_dict: Словарь, содержащий результат анализа в виде {'Показатель': Количество}
        Пример:
        >>> blood_test = BloodTest("Анализ крови", "Иванов Иван Иванович", 12345, {'Гемоглобин': 140, 'Глюкоза': 4.3, 'Холестерин': 5.7})
        >>> print(blood_test)
        Исследование: Анализ крови. Пациент: Иванов Иван Иванович.
        >>> print(repr(blood_test))
        BloodTest(test='Анализ крови', patient='Иванов Иван Иванович', sample_code=12345)
     """

    def __init__(self, test: str, patient: str, sample_code: int, indicator_dict: dict[str, int]):
        super().__init__(test=test, patient=patient)
        self._sample_code = sample_code
        self._indicator_dict = indicator_dict

    def __repr__(self):
        return f"{self.__class__.__name__}(test={self._test!r}, patient={self._patient!r}, sample_code={self._sample_code!r})"

    # Метод __str__ унаследован

    @property
    def sample_code(self):
        """Возвращает код пробирки"""
        return self._sample_code

    @sample_code.setter
    def sample_code(self, code: int) -> None:
        """ Устанавливает код пробирки"""
        if not isinstance(code, int):
            raise TypeError("Код пробирки должен быть целым числом (int)!")
        elif code <= 0:
            raise ValueError("Код пробирки должен быть положительным числом!")
        self._sample_code = code

    @property
    def indicator_dict(self):
        """Возвращает результат анализа"""
        return self._indicator_dict

    @indicator_dict.setter
    def indicator_dict(self, result_dict: dict[str: float]) -> None:
        """ Записывает результат анализа"""

        if not isinstance(result_dict, dict):
            raise TypeError("Результат анализа должен быть представлен в виде листа [Количество]!")
        for indicator, amount in result_dict.items():
            if not isinstance(indicator, str):
                raise TypeError("Название показателя должно быть типом str!")
            if not isinstance(amount, float):
                raise TypeError("Количество показателя должно быть типом float!")
            elif amount <= 0:
                raise ValueError("Количество показателя должно быть положительным числом!")
        self._indicator_dict = result_dict

    def out_of_norm(self) -> dict[str, int]:
        """ Метод, создающий словарь с парами показатель-значение, в которых значение оказалось больше или меньше нормы."""
        ...

    # Статический метод warning() унаследован

    @staticmethod
    def preparation_info() -> str:
        # Метод перегружен, так как нужно вывести другую информацию
        """ Метод, выводящий информацию о необходимой подготовке к исследованию"""
        return "Кровь сдается в утренние часы натощак. За 1-2 дня до исследования исключить из рациона продукты с высоким содержанием жиров."


if __name__ == "__main__":
    some_test = MedTest("Анализ мочи", "Иванов Иван Иванович")
    print(some_test)
    print(repr(some_test))
    blood_test = BloodTest("Анализ крови", "Иванов Иван Иванович", 12345, {'Гемоглобин': 140, 'Глюкоза': 4.3, 'Холестерин': 5.7})
    print(blood_test)
    print(repr(blood_test))
    pass

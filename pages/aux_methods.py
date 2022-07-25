from random import choice
from string import ascii_letters, digits


class AuxMetods:
    """Класс вспомогательных методов, которые используются в параметризации, для добавления различных строк и цифр"""

    @staticmethod
    def generate_string(factor: int) -> str:
        return "x" * factor

    @staticmethod
    def russian_chars() -> str:
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    @staticmethod
    def english_chars() -> str:
        return 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def random_chars(length: int) -> str:
        random_str = ''.join(choice(ascii_letters) for i in range(length))
        return random_str

    @staticmethod
    def random_num(length: int) -> int:
        random_int = int(''.join(choice(digits) for i in range(length)))
        return random_int

    @staticmethod
    def random_phone(length: int) -> str:
        rand_phone = f"73{''.join(choice(digits) for i in range(length - 2))}"
        return rand_phone

    @staticmethod
    def chinese_chars() -> str:
        return '的一是不了人我在有他这为之大来以个中上们'

    @staticmethod
    def special_chars() -> str:
        return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
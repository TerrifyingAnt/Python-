class Num:
    """Класс содержит в себе объект числа"""

    def __init__(self, number):
        self.number = number
        self.inside = number

    def __str__(self):
        return str(self.number)

    def get_inside(self):
        return self.inside

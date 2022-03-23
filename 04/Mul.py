from Num import Num


class Mul(Num):
    """Класс реализует операцию умножения"""

    def __init__(self, x: Num, y: Num):
        self.number = x.number * y.number
        self.inside = [x.get_inside(), "*", y.get_inside()]

    def __str__(self):
        return "MUL"

    def get_inside(self):
        return self.inside








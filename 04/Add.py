from Num import Num


class Add(Num):
    """Класс реализует операцию сложения"""

    def __init__(self, x: Num, y: Num):
        self.number = x.number + y.number
        self.inside = [x.get_inside(), "+", y.get_inside()]

    def __str__(self):
        return "ADD"

    def get_inside(self):
        return self.inside

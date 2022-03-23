from Num import Num

class StackVisitor:
    """Класс, реализующий работу стека"""

    def __init__(self):
        self.stack = []

    def visit(self, x: Num):
        for token in self.stack:
            print(token)



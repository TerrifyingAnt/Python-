from Num import Num



class PrintVisitor:
    """Класс реализующий вывод выражения"""

    def __init__(self):
        self.tokens = []
        self.expr = []


    def visit(self, expr: Num):
        self.expr = expr.get_inside()
        return str(self.expr).replace("[", "(").replace("]", ")").replace(",", "").replace("'", "")


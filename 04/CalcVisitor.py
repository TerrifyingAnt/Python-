from Num import Num
import re

class CalcVisitor:
    """Класс реализующий вычисления"""

    def __init__(self):
        self.tokens = []

    def visit(self, expr: Num):
        self.tokens = re.split(" ", str(expr.get_inside()).replace("[", "( ")
                               .replace("]", " ) ").replace(",", "").replace("'", ""))
        k = self.tokens.count("")
        for i in range(k):
            self.tokens.remove("")
        print(self.tokens)
        open_s, close_s = [0], [-1]
        open_count = self.tokens.count("(")
        new_open_list = []
        for i in range(open_count):
            new_open_list.append(i)
            open_s.append(i * str(self.tokens[i]).find("(", open_s[len(open_s) - 1] + 1))
            open_count -= 1
            close_s.append(str(self.tokens).replace("[", "").replace("]", "").replace(",", "").replace("'", "")
                           .find(")", close_s[len(close_s) - 1]))
        open_s.remove(0)
        close_s.remove(-1)
        print(str(self.tokens).replace("[", "").replace("]", "").replace(",", "").replace("'", "").find(")", close_s[len(close_s) - 1]))
        templist = []
        movements = []
        for i in range(len(open_s)):
            for j in range(i, int(close_s[i]) - i):
                templist.append(self.tokens[j])
            movements.append(templist)
            templist.clear()

        return movements



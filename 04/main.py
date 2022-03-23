from Num import Num
from Mul import Mul
from Add import Add
from PrintVisitor import PrintVisitor
from CalcVisitor import CalcVisitor



x = Add(Mul(Num(10), Num(15)), Add(Num(1), Mul(Num(2), Num(3))))
pv = PrintVisitor()
cv = CalcVisitor()
print(pv.visit(x))
print(cv.visit(x))

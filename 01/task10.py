def fast_mul(x, y):
    """Умножение по методу русского крестьянина"""
    sum = 0
    while x > 0:
        if x % 2 != 0:
            sum += y
        x //= 2
        y *= 2
    return sum


def fast_pow(x, y):
    """Возведение в степень по методу русского крестьянина"""
    sum = 1
    while y > 0:
        if y % 2 != 0:
            sum *= x
        y //= 2
        x *= x
    return sum


def fast_mul_gen(x):
    """Генератор задач"""
    y = 1
    new_x = x
    sum = 0
    i = 0
    while x > 0:
        i += 1
        if x % 2 != 0:
            sum += y
        x //= 2
        y *= 2
    return "Представим, что в Питоне отсутствует операция умножения. " \
           "Ее можно заменить сложением. Если мы хотим умножить какое-то число x на 12, " \
           "то нам понадобится 11 сложений, правильно? Но можно обойтись меньшим числом сложений. " \
           "Попробуйте составить программы для умножения на " + str(new_x) + " за " + str(i) + " сложений\n"


assert fast_mul(29, 2) == 58
assert fast_mul(29, 3) == 87
assert fast_pow(2, 2) == 4
assert fast_pow(3, 5) == 243
print(fast_mul_gen(12))
print(fast_mul_gen(16))
print(fast_mul_gen(15))
print(fast_mul_gen(29))

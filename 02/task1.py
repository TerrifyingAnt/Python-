def task_one(s):
    """Преобразовать элементы списка s из строковой в числовую форму."""
    return list([int(x) for x in s if x.isdigit()])


def task_two(s):
    """Подсчитать количество различных элементов в последовательности s."""
    return len(set(s))


def task_three(s):
    """ Обратить последовательность s без использования функций."""
    return s[::-1]


def task_four(s, x):
    """Выдать список индексов, на которых найден элемент x в последовательности s."""
    return list([int(i) for i in range(len(s)) if s[i] == x])


def task_five(s):
    """Сложить элементы списка s с четными индексами."""
    return sum(list([int(s[i]) for i in range(len(s)) if i % 2 == 0]))


def task_six(s):
    """Найти строку максимальной длины в списке строк s."""
    return s[list([i for i in range(len(s)) if len(s[i]) == max(list([len(x) for x in s]))])[0]]


assert task_one("2314sdfqwer234") == [2, 3, 1, 4, 2, 3, 4]
assert task_two("11111222222222233333444sdf") == 7
assert task_three("example") == "elpmaxe"
assert task_four("qwerqtyq", "q") == [0, 4, 7]
assert task_five("123456789") == 25
assert task_six(["Somebody", "once", "told", "me", "the", "world", "is", "gonna", "roll", "me"]) == "Somebody"

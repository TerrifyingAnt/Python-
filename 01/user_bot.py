def script(check, x, y):
    if check("gold", x, y):
        return "take"
    # проверка на золото
    if (check("gold", x + 1, y) or check("gold", x + 2, y)) and not check("wall", x + 1, y):
        return "right"
    if (check("gold", x, y + 1) or check("gold", x, y + 2)) and not check("wall", x, y + 1):
        return "down"
    if (check("gold", x, y - 1) or check("gold", x, y - 2)) and not check("wall", x, y - 1):
        return "up"
    if (check("gold", x - 1, y) or check("gold", x - 2, y)) and not check("wall", x - 1, y):
        return "left"

    # внутренние углы
    if check("wall", x - 1, y) and check("wall", x, y - 1):
        return "right"
    if check("wall", x + 1, y) and check("wall", x, y - 1):
        return "down"
    if check("wall", x + 1, y) and check("wall", x, y + 1):
        return "left"
    if check("wall", x - 1, y) and check("wall", x, y + 1):
        return "up"

    # внешние углы
    if not check("wall", x, y - 1) and not check("wall", x - 1, y) and not check("wall", x + 1, y) and not check(
            "wall", x, y + 1):
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1):
            return "right"
        if check("wall", x + 1, y + 1):
            return "down"
        if check("wall", x - 1, y + 1):
            return "left"

    # движение между двух стен
    if check("wall", x, y - 1) and check("wall", x + 1, y - 1) and check("wall", x, y + 2):
        return "down"
    if check("wall", x, y + 1) and check("wall", x - 1, y + 1) and check("wall", x, y - 2):
        return "up"

    # движение по прямой
    if check("wall", x, y - 1):
        return "right"
    if check("wall", x - 1, y):
        return "up"
    if check("wall", x + 1, y):
        return "down"
    if check("wall", x, y + 1):
        return "left"
    return "pass"

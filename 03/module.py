x = 0


def hello():
    global x
    print("Ohayo!")
    x += 1


def get_x():
    global x
    print(x)
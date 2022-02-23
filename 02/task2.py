def long_variant():
    """24 символа"""
    i = 0
    return['much', 'code', 'wow'][i]


def short_variant():
    """17 символов"""
    return 'muchcodewow'[:4]


assert long_variant() == "much"
print(short_variant())
assert short_variant() == "much"

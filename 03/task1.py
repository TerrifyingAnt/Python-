def whitespace_before_error ():
    return True


def missing_whitespace_around_operator():
    return 1 +1


def missing_whitespace_after():
    return [1,2,3]


def unexpected_spaces_around_keyword_parameter_equals():
    print(True, end = '\n')

def expected_two_blank_lines_found_one():
    return True


def multiple_statements_on_one_line_colon():
    if True: return True


def multiple_statements_on_one_line_semicolon():
    if True: return True; else: return False


def comparison_to_none(cond):
    if cond == None:
        return True


def comparison_to_true(cond):
    if cond == True:
        return True

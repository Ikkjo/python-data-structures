from stack import Stack
from stack import EmptyStackException

ALLOWED_OPERANDS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ALLOWED_OPERATORS = ['+', '-', '*', '/', '^']

operator_priority = {'(': 0,
                     '+': 1,
                     '-': 1,
                     '*': 2,
                     '/': 2,
                     '^': 3}


def is_otvorena_z(token):
    if token == '(':
        return True
    return False


def is_zatvorena_z(token):
    if token == ')':
        return True
    return False


def is_higher_prio(first_o, second_o):
    global operator_priority
    if operator_priority[second_o] > operator_priority[first_o]:
        return True
    return False


def user_in():

    infix_expr = input('Unesite aritmeticku operaciju\n>>>')

    result = in_to_post(infix_expr)

    print(result)

def in_to_post(infix_expr):
    global ALLOWED_OPERANDS
    global ALLOWED_OPERATORS

    operator_stack = Stack()

    ret_str = ''

    for token in infix_expr:
        if token in ALLOWED_OPERANDS:
            ret_str += token


        if is_otvorena_z(token):
            operator_stack.push(token)

        if is_zatvorena_z(token):
            pop = operator_stack.pop()
            while not is_otvorena_z(pop):
                ret_str += " " + pop + " "
                pop = operator_stack.pop()

        elif token in ALLOWED_OPERATORS:
            ret_str += " "

            while True:

                if operator_stack.is_empty() or is_otvorena_z(operator_stack.top()):
                    operator_stack.push(token)
                    break

                else:
                    if is_higher_prio(operator_stack.top(), token):
                        operator_stack.push(token)

                    else:
                        ret_str += " " + operator_stack.pop() + " "
                        break


    while not operator_stack.is_empty():
        ret_str += " " + operator_stack.pop() + " "

    # TODO: Ne radi, pokusaj sutra ponovo

    return ret_str
        # elif is_otvorena_z(token):
        #     pass
        # else:
        #     raise SyntaxError

if __name__ == '__main__':
    user_in()
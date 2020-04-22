from stack import Stack



def user_in():
    while True:
        try:
            number = eval(input('Input the number (positive whole number in base 10) for conversion: '))
            while not (isinstance(number, int) and number>=0):
                number = eval(input('Error, {0} is not a whole number!\n'
                                    'Try again: '.format(number)))
            break

        except Exception:
            print('Error, that is not a number! Try again. ')

    base = eval(input('Input the base for conversion (2-16): '))
    while not (isinstance(base, int) and (2 <= base <= 16)):
        base = eval(input('Error, {0} is not a whole number between 2 and 16!\n'
                          'Try again: '.format(base)))

    converted = convert_from_base10(number, base)

    print('{0} (base 10) is {1} in base {2}'.format(number, converted, base))
    return

def convert_from_base10(number, base):

    if number == 0:
        return '0'

    if base == 10:
        return str(number)

    symbols = '0123456789ABCDEF'

    s = Stack()

    while number != 0:

        base_mod = number % base

        symbol_to_push = symbols[base_mod]

        s.push(symbol_to_push)

        number = number // base

    ret_string = ''

    while len(s) != 0:
        ret_string += s.pop()

    return ret_string


if __name__ == '__main__':
    user_in()
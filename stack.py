class StackError(Exception):
    """Base class for errors elated to Stack class"""
    pass


class EmptyStackException(StackError):
    """:raises Empty stack exception"""
    pass


class Stack(object):

    def __init__(self):
        self._data = []
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):

        return str(self._data)


    def is_empty(self):
        """
        Checks if stack is empty
        :return True if stack is empty, False if it is not empty
        """
        if self._length == 0:
            return True

        return False

    def push(self, item):

        """
        :param item: Item you want to put on the stack
        """

        self._data.insert(0, item)

        self._length += 1

    def pop(self):

        """
        :return: Item from the top of the stack, CHANGES STACK
        """

        if self._length == 0:
            raise EmptyStackException('Stack is empty!')

        # Povratna vrednost je prvi clan steka (poslednji dodat clan u listi)
        ret_val = self._data[0]

        # Moramo azurirati stek da ne ukljucuje sadasnji prvi clan zato sto se popuje
        new_data = self._data[1:]

        # dDodela atributu data novu vrednost steka
        self._data = new_data

        self._length -= 1

        return ret_val

    def top(self):

        """
        :return: Item from the top of the stack, DOESN'T CHANGE STACK
        """

        if self._length == 0:
            raise EmptyStackException('Stack is empty!')

        return self._data[-1]


# if __name__ == '__main__':
#     s = Stack()
#     for i in range(100000):
#         s.push(i)
#     s.push(2)
#     s.push(8)
#     s.push('D')
#     s.push(3.332)
#     print(s)
#     print("Popped", s.pop())
#     print(s.top())
#     print(len(s))
#
#     s.pop()
#     print(s.is_empty())

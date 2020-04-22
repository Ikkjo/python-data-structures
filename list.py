# =========================================================================

class UnoNode(object):

    """
    Node za singly linked listu
    """


    def __init__(self, value):
        self._value = value
        self._next = None

    def __next__(self):
        return self._next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __eq__(self, other):
        return self._value == other.value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value

    def set_next(self, next_node):
        self._next = next_node


class SLinkedList(object):

    """
    Singly linked list

    """

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current
            current = next(current)

    def __str__(self):
        if self._size == 0:
            return "[]"
        else:
            ret_str = "["

            for item in self:
                if len(ret_str) != 1:
                    ret_str += ', '

                if isinstance(item, str):
                    ret_str += '"' + item + '"'
                else:
                    ret_str += str(item)

            ret_str += "]"

            return ret_str

    def __getitem__(self, index):

        if index < 0:
            index += self._size

        if index > self._size - 1:
            raise IndexError

        ret_element = self._head
        counter = 0
        while counter != index:
            ret_element = next(ret_element)
            counter += 1

        return ret_element

    def __setitem__(self, index, value):
        new_node = UnoNode(value=value)

        new_node.set_next(next(self[index]))

        self[index - 1].set_next(new_node)

    def __delitem__(self, index):
        if index < 0:
            index += self._size

        if index > self._size - 1:
            raise IndexError

        elif index == 0:
            self._head = self[1]

        elif index == self._size - 1:
            self[-1].set_next(None)

        else:
            self[index - 1].set_next(self[index + 1])
            self._size -= 1

    def is_empty(self):
        return self._size == 0

    def extend(self, s_linked_list):
        if len(s_linked_list) != 0:
            self[-1].set_next(s_linked_list[0])

    def append(self, value):

        node_to_append = UnoNode(value)

        if not self._head:
            self._head = node_to_append

        else:
            current = self._head
            while next(current):
                current = next(current)

            current.set_next(node_to_append)

        self._size += 1

    def remove(self, value):

        for item in self:
            if item == value:
                item.set_value(value)
                return

        raise ValueError("LinkedList doesn't contain an item of that value!")

    def insert(self, index, value):

        if index < 0:
            index += self._size

        if index > self._size - 1:
            raise IndexError

        if index == self._size - 1:
            self.append(value)
            return

        new_node = UnoNode(value)

        if index == 0:
            previous_head = self._head
            new_node.set_next(previous_head)
            self._head = new_node

        else:

            self[index - 1].set_next(new_node)
            new_node.set_next(self[index])


# ============================================================================================================

class DuoNode(UnoNode):

    def __init__(self, value):
        super().__init__(value)
        self._previous = None

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, new_previous):
        self._previous = new_previous


class DoublyLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, item):
        node = DuoNode(item)

        if self._size == 0:
            self._head = node
            self._tail = node

        else:
            self._tail.next = node
            self._tail = node


        self._size += 1

    def remove(self, item):

        current = self._head

        while current is not None:

            if current.value == item:

                one_before_node = current.previous
                one_after_node = current.next
                one_before_node.next = one_after_node

                self._size -= 1
                return True

            current = current.next

        raise ValueError("This DoublyLinkedList doesn't contain an item of that value!")

    def insert(self, index, item):

        node = DuoNode(item)

        current = self._head
 













if __name__ == '__main__':

    a = DoublyLinkedList()

    a.append("burek")

    a.append("pica")

    a.append("pica burek :O")

    pass

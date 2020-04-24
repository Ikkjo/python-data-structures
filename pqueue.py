from list import SLinkedList

class PQErrors(Exception):
    """Base class for PQErrors"""

class PQEmptyException(PQErrors):
    """Raised when Queue is empty"""

class PQItem(object):

    def __init__(self, key=None, value=None):
        self._key = key
        self._value = value

    def __lt__(self, other):
        return self._key < other.key

    def __le__(self, other):
        return self._key <= other.key

    def __eq__(self, other):
        return self._key == other.key

    def __str__(self):
        return "({0}: {1})".format(self._key, self._value)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class PQueue(object):

    def __init__(self):
        self._pqueue = SLinkedList()

    def __len__(self):
        return len(self._pqueue)

    def is_empty(self):
        return len(self._pqueue) == 0

    def first(self):
        return self._pqueue[0]


class SortedPQueue(PQueue):
    def __init__(self):
        super(SortedPQueue, self).__init__()

    def __len__(self):
        return super(SortedPQueue, self).__len__()

    def is_empty(self):
        return super(SortedPQueue, self).is_empty()

    def first(self):
        return super(SortedPQueue, self).first()

    def add(self, key, value):

        newest = PQItem(key, value)

        current = self.first()

        while current is not None and current < newest:
            current = next(current)

        if current is None:
            self._pqueue.insert(0, newest)
        else:
            index = self._pqueue.index(current)
            self._pqueue.insert(index, newest)

    def remove_min(self):
        if self._pqueue.is_empty():
            raise PQEmptyException("Priority queue is empty!")












class DeQueueError(Exception):
    """Base class for errors elated to Stack class"""
    pass


class EmptyDeQueueException(DeQueueError):
    """:raises Empty stack exception"""

class Deq(object):

    def __init__(self):

        """
        Double-ended queue has dequeue and length attributes. Dequeue is a container (type: list) in which the items
        (data) are put in or removed from. The attribute length (int) is the length of the queue.

        """

        self._dequeue = []
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._dequeue)

    def add_first(self, item):

        """Inserts item at the beginning of the de-queue, counter for length increases by 1"""

        self._dequeue.insert(0, item)
        self._length += 1


    def add_last(self, item):

        """Inserts item at the end of the de-queue, counter for length increases by 1"""

        self._dequeue.append(item)

        self._length += 1

    def delete_first(self):

        """
        Deletes first item from de-queue

        :returns First item in queue

        :raises EmptyDeQueueException if de-queue is empty"""

        if self._length == 0:
            raise EmptyDeQueueException('Double-ended queue is empty!')

        first = self._dequeue[0]

        self._dequeue = self._dequeue[1:]

        self._length -= 1

        return first

    def delete_last(self):

        """
        Deletes last item in de-queue

        :returns Last item in queue

        :raises EmptyDeQueueException if de-queue is empty
        """

        if self._length == 0:
            raise EmptyDeQueueException('Double-ended queue is empty!')

        last = self._dequeue[-1]

        self._dequeue = self._dequeue[:-1]

        self._length -= 1

    def first(self):

        """:returns First item in de-queue"""

        return self._dequeue[0]

    def last(self):

        """:returns Last item in de-queue"""

        return self._dequeue[-1]

    def is_empty(self):
        """:returns True if de-queue is empty, False if it is not empty"""

        if self._length == 0:
            return True
        return False
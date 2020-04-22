from queue import Queue


class TreeNode(object):

    def __init__(self, value=None, parent=None):
        self._value = value
        self._parent = parent
        self._children = []

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return self != other

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, node):
        node.parent = self
        self._children.append(node)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def is_leaf(self):
        return len(self._children) == 0

    def iterate_children(self, node):
        for child in node.children:
            yield child


class Tree(object):

    def __init__(self, root=None):

        self._root = root
        self._length = 0 if root is None else 1

    def __len__(self):
        return self._length

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, new_root):
        self._root = new_root

    def is_empty(self):
        return True if self._root is None else False

    def is_root(self, node):
        return node == self._root

    def parent(self, node):
        return node.parent

    def postorder(self, function):
        self._postorder(self._root, function)

    def _postorder(self, node, function):

        for child in node.children:
            self._postorder(child, function)

        function(node)

    def preorder(self, function):
        self._preorder(self._root, function)

    def _preorder(self, node, function):

        function(node)

        for child in node.children:
            self._preorder(child, function)

    def breadth_first(self, function):
        queue = Queue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            node = queue.dequeue()
            function(node)
            for child in node.children:
                queue.enqueue(child)

def make_tree(root_value):
    root = TreeNode(value=root_value)
    tree = Tree(root)
    return tree



if __name__ == '__main__':
    a = make_tree(22)
    root = a.root

    root.child = ()






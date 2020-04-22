from queue import Queue

class BTNodeException(Exception):
    """Base class for BTNode Exceptions"""
    pass


def check_if_btnode(obj):
    if not isinstance(obj, BTNode):
        raise TypeError("Object must be BTNode data type!")


class BTNode(object):

    def __init__(self, data, parent=None, l_child=None, r_child=None):
        self._data = data
        self._parent = parent
        self._r_child = r_child
        self._l_child = l_child

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        eq_data = self._data == other.value
        eq_parent = self._parent == other.value
        eq_rchild = self._r_child == other.r_child
        eq_lchild = self._l_child == other.l_child

        return eq_lchild and eq_rchild and eq_parent and eq_data

    def __ne__(self, other):
        eq_data = self._data != other.value
        eq_parent = self._parent != other.value
        eq_rchild = self._r_child != other.r_child
        eq_lchild = self._l_child != other.l_child
        return eq_lchild and eq_rchild and eq_parent and eq_data

    def is_leaf(self):
        return self._l_child is None and self._r_child is None

    def is_root(self):
        return self._parent is None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        check_if_btnode(new_parent)
        self._parent = new_parent

    @property
    def r_child(self):
        return self._r_child

    @r_child.setter
    def r_child(self, new_r_child):
        check_if_btnode(new_r_child)
        self._r_child = new_r_child

    @property
    def l_child(self):
        return self._l_child

    @l_child.setter
    def l_child(self, new_l_child):
        check_if_btnode(new_l_child)
        self._l_child = new_l_child

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class BinaryTree(object):

    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, new_root):
        self._root = new_root

    def is_empty(self):
        return self._root is None

    def is_root(self, node):
        return node == self._root

    def preorder(self, function):
        self._pretorder(function, self._root)

    def _preorder(self, function, node):

        function(node)

        if node.l_child is not None:
            self._preorder(function, node.l_child)

        if node.r_child is not None:
            self._preorder(function, node.r_child)

    def inorder(self, function):
        self._inorder(function, self._root)

    def _inorder(self, function, node):

        if node.l_child is not None:
            self._preorder(function, node.l_child)

        function(node)

        if node.r_child is not None:
            self._preorder(function, node.r_child)

    def postorder(self, function):
        self._postorder(function, self._root)

    def _postorder(self, function, node):

        if node.l_child is not None:
            self._preorder(function, node.l_child)

        if node.r_child is not None:
            self._preorder(function, node.r_child)

        function(node)

    def breadth_first(self, function):
        queue = Queue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            node = queue.dequeue()
            function(node)
            if node.l_child is not None:
                queue.enqueue(node.l_child)
            if node.r_child is not None:
                queue.enqueue(node.r_child)

def make_btree(root_data):
    bt_root = BTNode(root_data)
    return BinaryTree(bt_root)


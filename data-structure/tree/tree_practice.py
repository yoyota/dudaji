class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left is not None:
            for elem in self.left:
                yield elem

        if self.right is not None:
            for elem in self.right:
                yield elem

    def __repr__(self):
        return repr(self.value) + ', ' + repr(self.left) + ', ' +repr(self.right)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return repr(self.root)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
            if root is None:
                return TreeNode(value)

            if value < root.value:
                root.left = self._insert(root.left, value)
            else:
                root.right = self._insert(root.right, value)

            return root


    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            raise KeyError(key)

        if root.value > key:
            found = self._search(root.left, key)
        elif root.value < key:
            found = self._search(root.right, key)
        else:
            return root.value

        return found

    def find_min(self, root):
        if root.left is None:
            return root.value
        self.find_min(root.left)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self._remove(root.left, value)
        elif value > root.value:
            root.right = self._remove(root.right, value)
        else:

            if not root.left and not root.right:
                root = None
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                right_min_value = self.find_min(root.right)
                root.value = right_min_value
                root.right = self._remove(root.right, right_min_value)

        return root


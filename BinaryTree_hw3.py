# File: BinaryTree_hw3.py
# Author(s): xingqil, xxx


class BinaryTree:
    class _BTNode:
        def __init__(self, value, left = None, right = None):
            self._value = value
            self._left = left
            self._right = right

    def __init__(self):
        self._top = None

    def __eq__(self, other):
        return str(self) == str(other)

    def __contains__(self, item):
        cur_node = self._top

        while cur_node is not None:
            if item == cur_node._value:
                return True
            elif item > cur_node._value:
                cur_node = cur_node._right
            else:
                cur_node = cur_node._left

        return False

    def __str__(self):
        return self._str_help(self._top)

    def _str_help(self, cur_node):
        if cur_node is None:
            return ''
        else:
            left_str = self._str_help(cur_node._left)
            right_str = self._str_help(cur_node._right)
            ret = str(cur_node._value)
            if left_str:
                ret = left_str + ' ' + ret
            if right_str:
                ret = ret + ' ' + right_str
            return ret

    def insert(self, value):
        if self._top is None:
            self._top = BinaryTree._BTNode(value)
        else:
            self._insert_help(self._top, value)

    def _insert_help(self, cur_node, value):
        if value < cur_node._value:
            if cur_node._left is None:
                cur_node._left = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._left, value)
        elif value > cur_node._value:
            if cur_node._right is None:
                cur_node._right = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._right, value)

    def sum(self):
        return self._sum_help(self._top)

    def _sum_help(self, cur_node):
        if cur_node is None:
            return 0
        else:
            return (self._sum_help(cur_node._left)
                    + cur_node._value
                    + self._sum_help(cur_node._right))

    def size(self):
        return self._size_help(self._top)

    def _size_help(self, cur_node):
        if cur_node is None:
            return 0
        else:
            return (self._size_help(cur_node._left)
                    + 1
                    + self._size_help(cur_node._right))

    def print_pretty(self):
        print(self._print_pretty_help(self._top, 0))

    def _print_pretty_help(self, cur_node, indent_num):
        if cur_node is None:
            return ""
        else:
            left_pretty_str = "\n" + self._print_pretty_help(cur_node._left, indent_num + 1)
            right_pretty_str = self._print_pretty_help(cur_node._right, indent_num + 1) + "\n"

            cur_str = "        " * indent_num + str(cur_node._value)

            if cur_node._left is not None:
                cur_str = cur_str + left_pretty_str
            if cur_node._right is not None:
                cur_str = right_pretty_str + cur_str

            return cur_str

    def depth(self):
        return self._depth_help(self._top)

    def _depth_help(self, cur_node):
        if cur_node is None:
            return 0
        else:
            return 1 + max(self._depth_help(cur_node._left), self._depth_help(cur_node._right))

    def min(self):
        if self._top is None:
            return None
        else:
            temp_node = self._top

            while temp_node._left is not None:
                temp_node = temp_node._left

            return temp_node._value

    def max(self):
        if self._top is None:
            return None
        else:
            temp_node = self._top

            while temp_node._right is not None:
                temp_node = temp_node._right

            return temp_node._value

    def mean(self):
        return self.sum() / self.size() if self._top is not None else None

    def copy(self):
        new_tree = BinaryTree()

        self._copy_help(self._top, new_tree)
        return new_tree

    def _copy_help(self, cur_node, new_tree):
        if cur_node is not None:
            new_tree.insert(cur_node._value)

            self._copy_help(cur_node._left, new_tree)
            self._copy_help(cur_node._right, new_tree)

    def negate(self):
        self._negate_help(self._top)

    def _negate_help(self, cur_node):
        if cur_node is None:
            return None

        cur_node._value *= -1
        cur_node._left, cur_node._right = self._negate_help(cur_node._right), self._negate_help(cur_node._left)

        return cur_node






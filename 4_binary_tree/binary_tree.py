from node import Node


class BinaryTree:
    """
    This class is a binary tree implementation.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):
        """
        You should implement this method.
        It should add a node to the binary tree.
        If a node with that value already exists, raise a ValueError
        :param node: The Node to add
        :return: None
        """
        # The root is None, so set the root to be the new Node.
        if not self.__root:
            self.__root = node
        else:
            # Start iterating over the tree.
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    # Raise a ValueError, because the node's value already exists.
                    raise ValueError("{} with that value "
                        "already exists". format(marker))
                elif node.value > marker.value:
                    # Move to the right in the tree.
                    if not marker.get_right():
                        marker.set_right(node)
                        return
                    else:
                        marker = marker.get_right()
                else:
                    # Move to the left in the tree.
                    if not marker.get_left():
                        marker.set_left(node)
                        return
                    else:
                        marker = marker.get_left()

    def find(self, value):
        """
        You should implement this method.
        It should locate a node with a given value, and return it.
        If the Node is not found, it should raise a LookupError

        :param value: The value of the Node to locate.
        :return: Node, the found Node
        """
        marker = self.__root
        while marker:
            if marker.value == value:
                return marker
            elif value > marker.value:
                marker = marker.get_right()
            else:
                marker = marker.get_left()
        else:
            raise LookupError('No items found '
                'with the value "{}"'.format(value))

    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        print(current_node.print_details())
        self.__print_inorder_r(current_node.get_right())

'''
nodes = [[{'apple': True}, 1],
         [{'orange': False}, 4],
         [{'peach': True}, 6],
         [{'pear': True}, 8],
         [{'banana': False}, 9]]

b = BinaryTree()
for node in [Node(*n) for n in nodes][:3]:
    node.print_details()
    b.add(node)

print 'In order:'
b.print_inorder()

print 'Find 1'
print b.find(1)
print 'Find 4'
print b.find(4)
print 'Find 6'
print b.find(6)
'''
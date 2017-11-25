from node import Node
from linkedlist import LinkedList


class LinkedQueue:
    """
    This class is a queue wrapper around a LinkedList.

    This means that methods like `add_to_list_start` should now be called `push`, for example.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__linked_list = LinkedList()

    def push(self, node):
        """
        You should implement this method.
        It should add a node to the linked list property.
        :param node: The Node to add
        :return: None
        """
        self.__linked_list.add_start_to_list(node)

    def pop(self):
        """
        You should implement this method.
        It should remove a node from the end of the linked list, and return
        the removed node.
        :return: Node, the last node of the linked list after being removed.
        """
        return self.__linked_list.remove_end_from_list()

    def find(self, name):
        return self.__linked_list.find(name)

    def print_details(self):
        self.__linked_list.print_list()

    def __len__(self):
        """
        You should implement this method.
        It should return the amount of Nodes in the linked list.
        :return:
        """
        return self.__linked_list.size()

'''
nodes = [Node(*x) for x in [['George', 9995554444],
                            ['Sarah', 8884442222],
                            ['John', 6662227777]]]
lq = LinkedQueue()
for node in nodes:
    lq.push(node)

lq.print_details()

print('Found {}'.format(lq.find('Sarah')))

try:
    print(lq.find('Foo'))
except LookupError as e:
    print(str(e))

count = 0
while len(lq) and count != 3:
    lq.pop()
    count += 1
    print '-- Content of LQ: --'
    lq.print_details()
'''
from node import Node


class LinkedList:
    """
    This class is the one you should be modifying!
    Don't change the name of the class or any of the methods.

    Implement those methods that current raise a NotImplementedError
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_list(self, node):
        """
        This method should add at the beginning of the linked list.
        """
        marker = self.get_root()
        self.__root = node
        node.set_next(marker)

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        """
        This method should find a node in the linked list with a given name.

        :param name: the name of the node to find in this list.
        :return: the node found, or raises a LookupError if not found.
        """
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        else:
            raise LookupError("Didn't find anyone by the name '{}'".format(name))

'''
nodes = [Node(*x) for x in [['George', '0123x', 1997],
                            ['Sarah', '4567x', 2001],
                            ['John', '8901x', 1984]]]
ll = LinkedList()
for node in nodes:
    ll.add_to_list(node)

ll.print_list()
print(ll.get_root())

print('Found {}'.format(ll.find('Sarah')))
print(ll.find('Foo'))
'''
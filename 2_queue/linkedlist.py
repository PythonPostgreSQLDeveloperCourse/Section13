from node import Node


class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        """
        You can reuse the method written for the previous assignment here.

        :param node: the node to add at the start
        :return: None
        """
        marker = self.get_root()
        node.set_next(marker)
        self.__root = node

    def remove_end_from_list(self):
        """
        Implement this method! It should:
        - Iterate over each node
        - Find both the second-to-last node and the last node
        - Set the second-to-last node's next to be None
        - Return the last node
        :return: the removed Node.
        """
        marker = self.get_root()
        while marker:
            next_node = marker.get_next()
            if next_node:
                if not next_node.get_next():
                    # print('Removing {}'.format(next_node))
                    marker.set_next(None)
                    return next_node
            else:
                self.__root = None
                return marker
            marker = next_node

    def print_list(self):
        marker = self.get_root()
        while marker:
            marker.print_details()
            marker = marker.get_next()
        else:
            print(None)

    def find(self, name):
        """
        You can reuse the method written for the previous assignment here.

        :param name: the name of the Node to find.
        :return: the found Node, or raises a LookupError if not found.
        """
        marker = self.get_root()
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        else:
            raise LookupError("Didn't find anyone by the name '{}'".format(name))

    def size(self):
        """
        You should implement this method!
        It should return the amount of Nodes in the list.
        :return: the amount of nodes in this list.
        """
        count = 0
        marker = self.get_root()
        while marker:
            count += 1
            marker = marker.get_next()
        return count

'''
nodes = [Node(*x) for x in [['George', 9995554444],
                            ['Sarah', 8884442222],
                            ['John', 6662227777]]]
ll = LinkedList()
for node in nodes:
    ll.add_start_to_list(node)

ll.print_list()
print('Root Node: {}'.format(ll.get_root()))

print('Found {}'.format(ll.find('Sarah')))

try:
    print(ll.find('Foo'))
except LookupError as e:
    print(str(e))

print('Length of LL before: {}'.format(ll.size()))

ll.remove_end_from_list()

print('Length of LL after: {}'.format(ll.size()))
print('Contents of LL after')
ll.print_list()
'''
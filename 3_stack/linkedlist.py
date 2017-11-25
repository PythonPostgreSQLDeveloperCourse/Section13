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
        You can reuse the method we implemented previously.
        """
        marker = self.get_root()
        node.set_next(marker)
        self.__root = node

    def remove_start_from_list(self):
        """
        Implement this method! It should:
        - If self.__root is None, raise a RuntimeError as the list is already empty
        - Create a variable which stores the root
        - Set self.__root to be equal to the root's next node
        - Return the variable created previously
        :return:
        """
        marker = self.get_root()
        if not marker:
            raise RuntimeError('LinkedList is empty')
        next_node = marker.get_next()
        self.__root = next_node
        return marker

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        """
        You can reuse the method we implemented previously.
        """
        marker = self.get_root()
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        else:
            raise LookupError("No items found containing text '{}'".format(text))

    def size(self):
        """
        You can reuse the method we implemented previously.
        """
        count = 0
        marker = self.get_root()
        while marker:
            count += 1
            marker = marker.get_next()
        return count

'''
nodes = list(map(Node, ['apple', 'orange', 'banana']))

ll = LinkedList()
for node in nodes:
    ll.add_start_to_list(node)

ll.print_list()
print('Root Node: {}'.format(ll.get_root()))

print('Found {}'.format(ll.find('banana')))

try:
    print(ll.find('bannana'))
except LookupError as e:
    print(str(e))

print('Length of LL before: {}'.format(ll.size()))

ll.remove_start_from_list()

print('Length of LL after: {}'.format(ll.size()))
print('Contents of LL after')
ll.print_list()
'''
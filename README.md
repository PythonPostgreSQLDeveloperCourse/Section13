# Data Structures and Algorithms

## Common Data Structures

- Queue
- Stack
- Set
- Binary Tree

## Linked List

- Base for other Data Structs
- A sequence of items
- Each item knows where the next item is
- Each element is a Node

***Design***

- 2 Classes
	+ Node (holds data and the next Node)
		* Head, first Node
	+ LinkedList (manages the Nodes, holds the first Node)
		* `add_to_list()` and `find(name)` Methods
		* Find a Node in the LinkedList given a search param
		* Add a new Node in the beginning of the LinkedList


## Queue

***Design***

- What does it do?
	+ `push()` Add a new Node at the end
		* is equivalent to `LinkedList.add_to_list()`
	+ `pop()` Remove an Node from beginning
		* new method
		* get last Node (second to the last Node points to)
		* set the last Node equal to None
	+ `size()` Find it's size
	+ `print()` Print contents
- FIFO


## Stack

***Design***

- What does it do?
	+ just like a `queue`
	+ instead of FIFO, LIFO
	+ add elem to the beginning
	+ remove elem from the beginning
	+ or add and remove from the end
	+ find the size
	+ print contents


## Binary Tree

***Design***

- What does it do?
	+ unlike list structures
	+ has a branching structure
	+ leaves or nodes
	+ node "points" have two child nodes
- Adding
	+ start at the root (top)
	+ larger nodes to the right, smaller to the left
	+ the left key will have a smaller key than the parent
	+ no duplicates
- Finding
	+ start at the root
	+ key of the node we are looking for is greater, go right
	+ smaller, go left
	+ if key of the node is null, not found
	+ key of the current node is equal to the node we are trying to find we have found the node

***Visualization***

- [Binary Tree Visualization](http://btv.melezinek.cz/binary-heap.html)
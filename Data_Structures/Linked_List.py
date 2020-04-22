"""In case of array/python list : both are linear order, individual element can be accessed very easily.
Binary search can be used on both if they are sorted.
But the disdvantage is that all elements have to be shifted to add an element in between and also to close the gap in case of deletion.
This can be time consuming and memory inefficient for large sequences.
Also Arrays are fixed in length. Lists are also internally python arrays. For large arrays blocking this big array can be really difficult.

Now comes Linked List : these are also linear, smaller memory allocations and no elements shifting in case of insert/delete.
But in case of search a particular element it has to traverse the entire LL.
When we add element in a python list its worst case is O(n) coz actually it creates a new array of length() + 1 but in LL its dynamic.

When to use LL: when there is dynamic data, large number of inserts/deletes.
When to prefer lists: when accessing element by index i.e O(1)"""

# Basic element in any datastructure is Node. Hence creating a node class. Each node must have a data and atleast one link to point to the next element.
# But in case of a single node(Orphan Node) or end of the DS next node may not exist so we set next_node link = None for covering all cases.
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Now creating a Linked list class using Node class to create the basic structure.
# Every LL starts with a head_node or ROOT and ends with the Tail Node with null link or no next node.
# if a Linked list is empty => head_node = None
# LL traversal : O(n)
# LL searching a node: O(n)
# LL Inserting element at beginning : O(1)
# LL Removing a Node : O(n)

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
# adding node to the begining
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
# code to represent node value in string format
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
# code to remove any node
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
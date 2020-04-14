"""In case of array/python list : both are linear order, individual element can be accessed very easily.
Binary search can be used on both if they are sorted.
But the disdvantage is that all elements have to be shifted to add an element in between and also to close the gap in case of deletion.
This can be time consuming and memory inefficient for large sequences.
Also Arrays are fixed in length. Lists are also internally python arrays. For large arrays blocking this big array can be really difficult.

Now comes Linked List : these are also linear, smaller memory allocations and no elements shifting in case of insert/delete.
But in case of search a particular element it has to traverse the entire LL."""

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
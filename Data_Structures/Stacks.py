"""
Stacks :
    1. Linear Data structure
    2. Follows Last In First Out (LIFO) also called as First In Last Out (FILO) protocol
    3. Addition or deletion happens from the same end i.e. Top of Stack and the opposite end is called Base.
    4. for methods like isEmpty(), len(), peek() => O(1)
    5. for methods like pop(), push() => O(n) but if done sequentially its O(1)
    Applications : In checking correct sequence for paranthesis, delimiters and mze problem etc.

    A stack can be represented using python List/arrray or Linked List.
    With large number of push and pops , it may require reallocation of memory as list uses array underneth (array have fixed memory from declaration)
    LL helps to overcome dynamic memory reallocation issue and  the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.

    Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.
"""
from node import Node

#Class definition for Node
# class Node:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node
#
#     def set_next_node(self, next_node):
#         self.next_node = next_node
#
#     def get_next_node(self):
#         return self.next_node
#
#     def get_value(self):
#         return self.value


# Add your Stack class below:
from node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the pizza stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Delivering " + item_to_remove.get_value())
            return item_to_remove.get_value()
        print("All out of pizza.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0


# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
pizza_stack.pop()

##Output
"""
Adding pizza #1 to the pizza stack!
Adding pizza #2 to the pizza stack!
Adding pizza #3 to the pizza stack!
Adding pizza #4 to the pizza stack!
Adding pizza #5 to the pizza stack!
Adding pizza #6 to the pizza stack!
No room for pizza #7!
The first pizza to deliver is pizza #6
Delivering pizza #6
Delivering pizza #5
Delivering pizza #4
Delivering pizza #3
Delivering pizza #2
Delivering pizza #1
All out of pizza.
"""
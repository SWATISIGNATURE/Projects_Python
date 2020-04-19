"""
Trees:
    1. storing hierarchical data with a directed flow > nodes hold data
    2. Nodes also store references to zero or more other tree nodes. Data moves down from node to node
    3. Tree grows downward & root node is at the very top followed by child Nodes and leafs.
    4. Nodes share the same parent node, which makes them siblings.
    5. When a node has no children, we refer to it as a leaf node.
    6. Each node will only ever have at most one parent i.e. No child node will have more than one parent.
Tree Varieties:
    1. Wide: parent nodes referencing many child nodes.
    2. Deep : with many parent-child relationships.
Each time we move from a parent to a child, we’re moving down a level.
Depending on the orientation we refer to this as the
    a. depth (counting levels down from the root node)
    b. height (counting levels up from a leaf node)

1. Binary Tree:
    1. Tree where each parent can have no more than two children, known as the left child and right child.
    2. If applied the below constraints it becomes Binary Search Tree:
        a. Left child values must be lesser than their parent.
        b. Right child values must be greater than their parent.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)
print("=>",root.value)
root.traverse()
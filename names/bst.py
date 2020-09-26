print('binary search')
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# python's stack and queues import
# from stack import Stack
# from queue import Queue
# from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # left until the end is reached. 
            if not self.left:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        else: 
            # Right until the end is reached.
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target) # left above return with else, right below return without else accomplishes the same. 


    # Return the maximum value found in the tree
    # Recursive (this creates more call stacks)
    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     return self.right.get_max()

    # iterative 
    def get_max(self):
        max_value = self.value
        current_node = self
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.right
        return max_value
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    

class BinarySearchTree(BSTNode):
    def __init__(self, value):
        super().__init__(value)


"""
This code is necessary for testing the `print` methods
"""
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)


import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # If there is a value
        if self.value:

            # Greater than = to, go right
            if value >= self.value:

                # If right has a value
                if self.right:

                    # Ram it through method again
                    self.right.insert(value)

                # Otherwise, plant the value there
                else:
                    self.right = BinarySearchTree(value)

            # Otherwise, go left
            else:

                # If left has a value
                if self.left:

                    # Ram it through method again
                    self.left.insert(value)

                # Otherwise, plant the value there
                else:
                    self.left = BinarySearchTree(value)

        # Otherwise, plant the value there
        else:
            self.value = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        # If current node is target (true)
        if self.value == target:
            return True

        # Greater than, check right
        if target > self.value and self.right:
            return self.right.contains(target)

        # Less than, check left
        if target < self.value and self.left:
            return self.left.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # If there's a value to the right
        if self.right:

            # Ram it through method again
            return self.right.get_max()

        # Otherwise, we're at our max
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        # If there's a value to the right
        if self.right:

            # Ram it through method again
            self.right.for_each(cb)

        # If there's a value to the left
        if self.left:

            # Ram it through method again
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

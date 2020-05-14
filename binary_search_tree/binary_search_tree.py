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


from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
         #start at root, check if something there, if not insert
         #if something at root, move dwon & compare val: IF MORE-GO RIGHT: IF LESS: GO LEFT
         #repeat until empty found then return valu
        if self.value is None:
            self.value.insert(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right =BSTNode(value)
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #when we start searching, self will be root(only 1 we have access to rn)
        #compare target against self
        #if target matches self.value: return True
        #if false: we need to go left or right to check, BUT nothing is left or right
        if target == self.value:
            return True #this is where we stop. 
            ##with recursion we need stopping point. then it will bubble back up the tree with correct value to where function was initially called
            #if target < self.value: go left
        if target < self.value:
            if not self.left: #if there is no node left to go to, its false, else continue to call contain function
                return False
            return self.left.contains(target) #call contains function in itself(recursion) with same target to repeat operation of comparison on the left/right
        #if target is greater than self.value:go right
        else:
            
            if not self.right:
                return False 
            return self.right.contains(target) #self.right and self.left are there own nodes, which mean they each have contain method on them to be able to run check operations onn each tree level until target is found a mtach, then true is returned
        

    # Return the maximum value found in the tree
    def get_max(self):
        #check for anything in tree
    #check right side for node and pos greater than
    #if greater, return fn on node
    #else return value
        if self.value is None:
            return None
        if self.right is None:
            return self.value #if nothing to tthe right means nothing bigger than root
        else:
            return self.right.get_max() #if something is to right run fn to compare

              
     


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
    #check for value on left side
    #if node, call fn on it
    #?need to return value?
    #repeat right
        
        if self.value is None:
            return None
        if self.value is not None:
            fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
    # Part 2 -----------------------
##DFS- uses stack (our own or call stack w recursion) LIFO
#--uses: backtracking, complete search, paths, goes deep.
##BFS - uses queue FIFO
#--uses: check If path exists between nodes, findings distance out or 'levels' away. goes wide
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(node.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

            


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            current = queue.pop()
            print(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

       

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) >0:
            current = stack.pop()
            print(current.value)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

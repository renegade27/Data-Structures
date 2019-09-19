import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  #  * `insert` adds the input value to the binary search tree, 
  # adhering to the rules of the ordering of elements in a binary search tree.
  def insert(self, value):
    current = self
    while current:
      if current.value <= value:
          if current.right is None:
            current.right = BinarySearchTree(value)
            return 
          current = current.right

      elif current.value > value:
          if current.left is None:
             current.left = BinarySearchTree(value)
             return
          current = current.left

#* `contains` searches the binary search tree for the input value, 
# returning a boolean indicating whether the value exists in the tree or not.
  def contains(self, target):
    current = self

    while current:
      if target == current.value:
        return True
      elif target > current.value:
          if current.right is None:
            return False
          current = current.right

      elif target < current.value:
          if current.left is None:
            return False
          current = current.left

#* `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    current = self

    while current.right is not None:
      current = current.right
    
    return current.value

  #* `for_each` performs a traversal of _every_ node in the tree, 
  # executing the passed-in callback function on each tree node value. 
  # There is a myriad of ways to perform tree traversal; 
  # in this case any of them should work.
  def for_each(self, cb):
    current = self
  
    cb(current.value)

    if current.left is not None:
      current.left.for_each(cb)
    if current.right is not None:
      current.right.for_each(cb)
  
  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self, node):
    #check left
    #if node on left, recursively go left
    if node.left:
      node.in_order_print(node.left)
    
    #if none left
    print(node.value)

    if node.right:
      # recursively go right
      node.in_order_print(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(node):
      
      #initialize queue
      queue = Queue() 
      #add current node to queue
      queue.enqueue(node)

      #while queue is not empty
      while queue.size > 0:
        #visit top node in queue
        #remove from queue
        current = queue.dequeue()
        #print and
        print(current.value)
        #push children to queue
        if current.left:
          queue.enqueue(current.left)
        if current.right:
          queue.enqueue(current.right)


  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
            
      #initialize stack
      stack = Stack() 
      #add current node to stack
      stack.push(node)

      #while stack is not empty
      while stack.size > 0:
        #visit top node in stack
        #remove from stack
        current = stack.pop()
        #print and
        print(current.value)
        #push children to stack
        if current.left:
          stack.push(current.left)
        if current.right:
          stack.push(current.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass
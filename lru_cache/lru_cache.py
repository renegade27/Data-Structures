from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.current = 0
    self.limit = limit
    self.storage = DoublyLinkedList()
    self.dict = {}
    pass

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    current = self.storage.head
    while current:
      if current.value == key:
        self.storage.move_to_front(current)
        return self.dict[key]
      current = current.next
    return None


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if key in self.dict.keys():
      self.dict.update({key: value})
      self.get(key)
      return
    
    if self.storage.__len__() == self.limit:
      oldKey = self.storage.remove_from_tail()
      self.storage.add_to_head(key)
      self.dict[key] = value
      self.dict.pop(oldKey)
      return
    
    self.storage.add_to_head(key)
    self.dict[key] = value
    return

    # First try, fail
    # if self.storage.__len__() == self.limit:
    #   if key in self.dict:
    #     self.dict.update({ key: value})
    #     self.storage.remove_from_tail()
    #     self.storage.add_to_head(ListNode(key))
    #     return
    #   oldKey = self.storage.remove_from_tail()
    #   self.storage.add_to_head(ListNode(key))
    #   for keys in self.dict.keys():
    #     if keys == oldKey:
    #       self.dict[key] = self.dict.pop(oldKey)
    #       return
    # else:
    #   if key in self.dict:
    #     self.dict.update({ key: value})
    #     self.storage.delete(ListNode(key))
    #     self.storage.add_to_head(ListNode(key))
    #   self.storage.add_to_head(ListNode(key))
    #   self.dict[key] = value




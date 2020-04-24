import sys
sys.path.append('G:\Data\Lambda\CS\Sprint-Challenge--Data-Structures-Python\\ring_buffer\doubly_linked_list.py')
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
        self.limit = limit
        self.size = 0
        self.lookup = {}
        self.storage = DoublyLinkedList()
    
    def get(self, key):
        if key in self.lookup:
            if self.lookup[key].value != None:
                self.recently_used(key)
                return self.lookup[key].value
            else: # if self.lookup[key] exists, and the object's value is none
                self.remove_key(key)
                return None
        else:
            return None
        
    def set(self, key, value):
        if key in self.lookup:
            self.lookup[key].value = value
            self.recently_used(key)
        else:
            self.size += 1
            self.storage.add_to_head(value)
            self.lookup[key] = self.storage.head
            if self.size > self.limit:
                self.remove_last()
    
    def recently_used(self,key):
        update_node = self.lookup[key]
        self.storage.move_to_front(update_node)
        
    def remove_key(self,key):
        del self.lookup[key]

    def remove_last(self):
        self.storage.tail.value = None
        self.storage.remove_from_tail()
        
        

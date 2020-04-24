from doubly_linked_list import DoublyLinkedList

# you can do this with just list nodes. you don't
# need the dll at all. Actually you can do it with sll nodes
# you only really ever move forward and the last node is connected to the first node


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        # self.storage.add_to_head(0)
        # self.current = self.storage.head
        self.current = None
        self.length = 0
        self.switch = 0

    def append(self, item):
        # After buffer is created append is simple:
        if self.switch == 1:
            self.current.value = item
            self.current = self.current.next

        # For the first time (creating the ring buffer)
        elif self.switch == 0:
            self.storage.add_to_tail(item)
            self.length += 1
            if self.length == self.capacity:
                self.current = self.storage.head
                self.storage.tail.next = self.storage.head 
                    # maybe this breaks the dll?    
                    # I don't think so because I'm not calling a method
                    # I'm setting a value directly
                    # sure it breaks encapsulation (?)
                self.switch = 1

        
        

        # the first time you go through 
        # keep track of length
        # when length == capacity. 
        # link the current node to the head node.
        # throw a switch 
            # does this do anything weird with the 
        # from there you have a ring and the loop is constant

        # set current value = item
        # move current pointer to point to next item
            # self.currentnode.next 
        
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        length = 0 
        while length < self.capacity:
            if current != None:
                list_buffer_contents.append(current.value)
                current = current.next
                length += 1
            else:
                break
        # TODO: Your code here
        # start from the head of the dll
        # while i < capacity
            # value = pointer.value
            # if value is not none
                # add value of head to list_buffer
            # move pointer to pointer.next


        return list_buffer_contents

# ----------------Stretch Goal-------------------

# using an array allows you to preallocate the memory 
# this means you can return a pointer to a block of memory 
# instead of traversing nodes in order to create a list
# to return for the get method

# what disadvantage normally found in arrays is overcome here??> 
    # not sure


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.pointer = 0
        self.capacity = capacity
        self.is_full = False
        pass

    def append(self, item):
        self.storage[self.pointer] = item
        self.pointer += 1
        if self.pointer == self.capacity: # this will be reached after setting the index of capacity -1
            self.pointer = 0
            self.is_full = True
        pass

    def get(self):
        if self.is_full:
            return self.storage
        else:
            return self.storage[:self.pointer] # everything up to the zeros

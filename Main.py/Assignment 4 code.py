class Node:
    def __init__(self, value=None, next=None, previous=None):
        self._value = value
        self._next = next
        self._previous = previous

    def set(self, value):
        self._value = value
        return self

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def get_previous(self):
        return self._previous

    def set_next(self, next):
        self._next = next
        return self

    def set_previous(self, previous):
        self._previous = previous
        return self


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add Elements to the List
    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node

    # Remove Elements from the List
    def remove(self, index):
        if self.head is None:
            raise IndexError("Removing from an empty list")
        
        current = self.head
        count = 0
        while current:
            if count == index:
                if current.get_previous():
                    current.get_previous().set_next(current.get_next())
                if current.get_next():
                    current.get_next().set_previous(current.get_previous())
                if current == self.head:
                    self.head = current.get_next()
                if current == self.tail:
                    self.tail = current.get_previous()
                return
            count += 1
            current = current.get_next()
        
        raise IndexError("Index out of range")

    # Retrieve Elements by Index
    def get(self, index):
        if self.head is None:
            raise IndexError("Getting from an empty list")
        
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.get_value()
            count += 1
            current = current.get_next()

        raise IndexError("Index out of range")

    # Check if the List is Empty
    def is_empty(self):
        return self.head is None

    # Return the First and Last Elements
    def first(self):
        if self.head:
            return self.head.get_value()
        return None

    def last(self):
        if self.tail:
            return self.tail.get_value()
        return None

    # Reverse the List
    def reverse(self):
        if self.head is None:
            return
        
        current = self.head
        previous = None
        self.tail = self.head
        
        while current:
            next_node = current.get_next()
            current.set_next(previous)
            current.set_previous(next_node)
            previous = current
            current = next_node
        
        self.head = previous


# Example Usage
linked_list = LinkedList()

# Add elements
linked_list.add(5)
linked_list.add(10)
linked_list.add(15)

# get elements by index
print(linked_list.get(0)) 
print(linked_list.get(2))  

# Check if list is empty
print(linked_list.is_empty())  

# Get the first and last elements
print(linked_list.first())  
print(linked_list.last())   

# Remove element at index 1 
linked_list.remove(1)

# Check list after removal
print(linked_list.get(0))  
print(linked_list.get(1))  

# Reverse the list
linked_list.reverse()
print(linked_list.get(0))  
print(linked_list.get(1))  
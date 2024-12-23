class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data
    
    def get_size(self):
        return self.size
    
    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append({
                'data': current.data,
                'has_next': current.next is not None
            })
            current = current.next
        return elements

class DequeLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.front is None
    
    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1
        return True
    
    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1
        return True
    
    def remove_front(self):
        if self.is_empty():
            return None
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return temp
    
    def remove_rear(self):
        if self.is_empty():
            return None
        temp = self.rear.data
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return temp
    
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data
    
    def get_size(self):
        return self.size
    
    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append({
                'data': current.data,
                'has_next': current.next is not None,
                'has_prev': current.prev is not None
            })
            current = current.next
        return elements
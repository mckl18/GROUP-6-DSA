class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_beginning(self):
        if self.head is None:
            return "List is empty."
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

    def remove_at_end(self):
        if self.head is None:
            return "List is empty."
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node

    def remove_at(self, data):
        if self.head is None:
            return "List is empty."
        elif self.head.data == data:
            self.remove_at_beginning()
            return f"Removed '{data}' from the list."
        elif self.tail.data == data:
            self.remove_at_end()
            return f"Removed '{data}' from the list."
        else:
            current_node = self.head
            while current_node.next and current_node.next.data != data:
                current_node = current_node.next

            if current_node.next is None:
                return f"'{data}' not found in the list."
            else:
                current_node.next = current_node.next.next
                return f"Removed '{data}' from the list."

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        elements = []
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

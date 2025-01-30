class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def get_size(self):
        return self.size

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2
    if operator == '^':
        return 3
    return 0

class ShuntingYard:
    def __init__(self):
        self.operator_stack = Stack()
        self.steps = []
        self.current_output = ""
    
    def add_step(self):
        self.steps.append(self.current_output)
    
    def infix_to_postfix(self, infix):
        tokens = [char for char in infix if char != ' ']
        self.current_output = ""
        self.steps = []
        
        for token in tokens:
            if token.isalnum():  
                self.current_output += token
                self.add_step()
            
            elif token == '(':
                self.operator_stack.push(token)
            
            elif token == ')':
                while (not self.operator_stack.is_empty() and 
                       self.operator_stack.peek() != '('):
                    self.current_output += self.operator_stack.pop()
                    self.add_step()
                self.operator_stack.pop() 
            
            else:  
                while (not self.operator_stack.is_empty() and
                       self.operator_stack.peek() != '(' and
                       precedence(token) <= precedence(self.operator_stack.peek())):
                    self.current_output += self.operator_stack.pop()
                    self.add_step()
                self.operator_stack.push(token)
        
        while not self.operator_stack.is_empty():
            op = self.operator_stack.pop()
            if op != '(':
                self.current_output += op
                self.add_step()
        
        return self.steps

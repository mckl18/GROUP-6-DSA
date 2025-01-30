from typing import Tuple

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        return False  

    def find_node(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left = self.find_node(node.left, value)
        return left if left else self.find_node(node.right, value)

    def insert_left(self, parent_value, value):
        parent = self.find_node(self.root, parent_value)
        if parent and parent.left is None:
            parent.left = Node(value)
            return True
        return False  

    def insert_right(self, parent_value, value):
        parent = self.find_node(self.root, parent_value)
        if parent and parent.right is None:
            parent.right = Node(value)
            return True
        return False  

    def delete_node(self, node, key):
        if node is None:
            return None
        if node.value == key:
            return None  

        node.left = self.delete_node(node.left, key)
        node.right = self.delete_node(node.right, key)
        return node

    def get_all_nodes(self, node):
        if node is None:
            return []
        return [node.value] + self.get_all_nodes(node.left) + self.get_all_nodes(node.right)

    def print_tree(self, node, prefix="", is_left=True):
        if not node:
            return "Empty Tree"
        tree_str = ""
        if node.right:
            tree_str += self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        tree_str += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"
        if node.left:
            tree_str += self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        return tree_str

    def print_tree_fancy(self, node: Node) -> str:
        if not node:
            return "Empty Tree"

        lines = []
        level = [node]
        while level and any(level):
            current_level = []
            next_level = []
            
            for n in level:
                if n:
                    current_level.append(str(n.value))
                    next_level.extend([n.left, n.right])
                else:
                    current_level.append(' ')
                    next_level.extend([None, None])
            
            if any(n is not None for n in next_level):
                lines.append(' '.join(current_level))
                level = next_level
            else:
                lines.append(' '.join(current_level))
                break

        return '\n'.join(['Level ' + str(i) + ': ' + line 
                         for i, line in enumerate(lines)])

    def print_artistic(self, node: Node) -> str:
        if not node:
            return "Empty Tree"

        def build_tree_string(node: Node, prefix: str = "", is_left: bool = True) -> str:
            if not node:
                return ""

            tree_str = ""
            if node.right:
                tree_str += build_tree_string(node.right, prefix + ("│   " if is_left else "    "), False)

            tree_str += prefix + ("└── " if is_left else "┌── ") + str(node.value) + "\n"

            if node.left:
                tree_str += build_tree_string(node.left, prefix + ("    " if is_left else "│   "), True)

            return tree_str

        return build_tree_string(node, "", True)

    def inorder_traversal(self, start: Node, traversal: str) -> str:
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + ' - '
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def change_node_value(self, root: Node, old_value: int, new_value: int) -> Tuple[Node, str]:
        if root is None:
            raise ValueError("The tree is empty, no node to change.")
        
        if root.value == old_value:
            root.value = new_value
            return root, f"Successfully changed value from {old_value} to {new_value}"
        
        left_result, left_message = self.change_node_value(root.left, old_value, new_value) if root.left else (None, "")
        right_result, right_message = self.change_node_value(root.right, old_value, new_value) if root.right else (None, "")
        
        if left_result is None and right_result is None:
            raise ValueError(f"Node with value '{old_value}' not found")

        return (left_result, left_message) if left_result else (right_result, right_message)

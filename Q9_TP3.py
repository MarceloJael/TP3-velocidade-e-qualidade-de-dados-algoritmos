class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    
    result = []
    
    def traverse(node):
        if node is not None:
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)
    
    traverse(root)
    return result

if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)

    result = in_order_traversal(root)
    print("Valores dos nós em ordem:", result)
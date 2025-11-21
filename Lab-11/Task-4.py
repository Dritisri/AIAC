class TreeNode:
    """
    Represents a node in the Binary Search Tree.
    Each node contains some data and pointers to its left and right children.
    """
    def __init__(self, value):
        """
        Initialize a tree node.
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Implements a Binary Search Tree with insert, search, and inorder_traversal methods.
    """

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        Args:
            value: The value to be inserted.
        """
        if self.root is None:
            self.root = TreeNode(value)
            print(f"Inserted {value} as root")
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Helper for recursive insertion.
        Args:
            node: Current node to compare.
            value: Value to insert.
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                print(f"Inserted {value} to left of {node.value}")
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
                print(f"Inserted {value} to right of {node.value}")
            else:
                self._insert_recursive(node.right, value)
        else:
            print(f"Value {value} already exists. No duplicates allowed in BST.")

    def search(self, value):
        """
        Search for a value in the BST.
        Args:
            value: The value to search for.
        Returns:
            True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper for recursive search."""
        if node is None:
            print(f"{value} not found in BST.")
            return False
        if value == node.value:
            print(f"Found {value} in BST.")
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST.
        Returns:
            List of values in inorder sequence.
        """
        result = []
        self._inorder_recursive(self.root, result)
        print("Inorder traversal:", " ".join(str(x) for x in result))
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    """
    Example usage of BinarySearchTree with insert, search, and inorder_traversal:
    """

    bst = BinarySearchTree()
    
    # Insert values
    print("Inserting values into BST:")
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    print("\nPerforming inorder traversal:")
    bst.inorder_traversal()      # Should print sorted order: 20 30 40 50 60 70 80
    
    print("\nSearching for values:")
    bst.search(60)                # Found
    bst.search(25)                # Not found
    bst.search(50)                # Found (root)

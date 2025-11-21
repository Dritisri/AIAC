class Node:
    """
    Represents a node in a singly linked list.
    Each node contains some data and a reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Implements a basic singly linked list with methods to:
    - Insert at the end
    - Delete a node by value
    - Traverse the list
    """
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the list.
        """
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} as the head.")
            return
        # Otherwise, traverse to the end and append
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end.")

    def delete_value(self, value):
        """
        Deletes the first node with the specified value.
        If the value does not exist, nothing happens.
        """
        current = self.head
        prev = None
        # Traverse the list to find the node to delete
        while current:
            if current.data == value:
                if prev:
                    # Bypass the current node
                    prev.next = current.next
                else:
                    # If deleting the head node
                    self.head = current.next
                print(f"Deleted node with value {value}.")
                return
            prev = current
            current = current.next
        print(f"Value {value} not found in the list.")

    def traverse(self):
        """
        Prints all elements in the list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty.")

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.traverse()           # Should show "List is empty."
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.traverse()           # 10 -> 20 -> 30
    sll.delete_value(20)
    sll.traverse()           # 10 -> 30
    sll.delete_value(100)    # Value not found
    sll.delete_value(10)
    sll.traverse()           # 30
    sll.delete_value(30)
    sll.traverse()           # List is empty.

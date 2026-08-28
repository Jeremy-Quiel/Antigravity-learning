from typing import List, Optional


class Node:
    """Represent one node in a binary search tree.

    Each node stores an integer and references to its left and right children.
    A missing child is represented by ``None``.
    """

    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    def __repr__(self) -> str:
        """Return a concise representation containing the node's value."""
        return f"Node({self.value})"


class BinarySearchTree:
    """Implement a binary search tree (BST) containing integer values."""

    def __init__(self):
        """Create an empty tree with no root node."""
        self.root: Optional[Node] = None

    # =========================================================================
    # INSERTION
    # =========================================================================
    def insert(self, value: int) -> None:
        """Insert an integer value into the tree if it is not already present."""
        if not isinstance(value, int):
            raise TypeError("The value must be an integer.")

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value: int) -> None:
        """Place a value recursively according to the BST ordering rule."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        else:
            # Existing values are ignored so the tree never contains duplicates.
            pass

    # =========================================================================
    # SEARCH
    # =========================================================================
    def search(self, value: int) -> Optional[Node]:
        """
        Search for a value and return its node, or ``None`` when it is absent.
        """
        if not isinstance(value, int):
            raise TypeError("The value to search for must be an integer.")
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: Optional[Node], value: int) -> Optional[Node]:
        """Search recursively by discarding the half that cannot contain value."""
        if current is None or current.value == value:
            return current

        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def contains(self, value: int) -> bool:
        """Return ``True`` when value exists in the tree; otherwise return ``False``."""
        return self.search(value) is not None

    # =========================================================================
    # DELETION
    # =========================================================================
    def delete(self, value: int) -> None:
        """Remove an integer value from the tree when it is present."""
        if not isinstance(value, int):
            raise TypeError("The value to delete must be an integer.")
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current: Optional[Node], value: int) -> Optional[Node]:
        """Delete value recursively and return the subtree's updated root."""
        if current is None:
            return None

        # Navigate toward the value using the BST ordering property.
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # The node to delete has been found.

            # Case 1: the node is a leaf with no children.
            if current.left is None and current.right is None:
                return None

            # Case 2: the node has exactly one child.
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Case 3: replace a node with two children by its in-order successor.
            successor = self._get_minimum(current.right)
            current.value = successor.value
            # Remove the successor from the right subtree after copying its value.
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _get_minimum(self, node: Node) -> Node:
        """Return the node with the smallest value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # =========================================================================
    # IN-ORDER TRAVERSAL
    # =========================================================================
    def inorder(self) -> List[int]:
        """Return all tree values in ascending order."""
        elements: List[int] = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(
        self, current: Optional[Node], elements: List[int]
    ) -> None:
        """Append values recursively in left-node-right order."""
        if current is not None:
            self._inorder_recursive(current.left, elements)
            elements.append(current.value)
            self._inorder_recursive(current.right, elements)


# =============================================================================
# EJEMPLO DE USO Y PRUEBAS
# =============================================================================
if __name__ == "__main__":
    tree = BinarySearchTree()

    print("=== Inserting values ===")
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(value)
    print(f"Inserted values: {values}")
    print(f"In-order traversal (sorted): {tree.inorder()}")

    print("\n=== Searching for values ===")
    for value in [40, 99]:
        result = tree.search(value)
        if result:
            print(f"Value {value} found in node: {result}")
        else:
            print(f"Value {value} not found in the tree.")

    print("\n=== Deleting values ===")
    print("1. Deleting leaf node (20)...")
    tree.delete(20)
    print(f"Current in-order traversal: {tree.inorder()}")

    print("2. Deleting node with one child (30)...")
    tree.delete(30)
    print(f"Current in-order traversal: {tree.inorder()}")

    print("3. Deleting node with two children (root: 50)...")
    tree.delete(50)
    print(f"Current in-order traversal: {tree.inorder()}")


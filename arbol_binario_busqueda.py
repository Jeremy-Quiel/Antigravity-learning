from typing import List, Optional


class Node:
  """Represents a single node within a binary search tree.

  Each node contains an integer value and references to its left and right
  children. A missing child is represented by ``None``.
  """

  def __init__(self, value: int):
    """Initialize a node with an integer value.

    :param value: The integer value to store in the node.
    """
    self.value: int = value
    self.left: Optional["Node"] = None
    self.right: Optional["Node"] = None

  def __repr__(self) -> str:
    """Return a string representation of the node."""
    return f"Node({self.value})"


class BinarySearchTree:
  """Implementation of a binary search tree (BST) for integer values."""

  def __init__(self):
    """Create an empty binary search tree without a root node."""
    self.root: Optional[Node] = None

  # =========================================================================
  # INSERTION
  # =========================================================================
  def insert(self, value: int) -> None:
    """Insert a new integer value into the tree.

    If the value already exists, duplicate insertion is ignored.
    :param value: The integer value to insert.
    :raises TypeError: If the value is not an integer.
    """
    if not isinstance(value, int):
      raise TypeError("The value must be an integer.")

    if self.root is None:
      self.root = Node(value)
    else:
      self._insert_recursive(self.root, value)

  def _insert_recursive(self, current: Node, value: int) -> None:
    """Recursively place a value adhering to binary search tree properties.

    :param current: The currently inspected node.
    :param value: The value to insert.
    """
    if value < current.value:
      # Smaller values belong in the left subtree
      if current.left is None:
        current.left = Node(value)
      else:
        self._insert_recursive(current.left, value)
    elif value > current.value:
      # Larger values belong in the right subtree
      if current.right is None:
        current.right = Node(value)
      else:
        self._insert_recursive(current.right, value)
    else:
      # Duplicates are ignored to preserve uniqueness
      pass

  # =========================================================================
  # SEARCH
  # =========================================================================
  def search(self, value: int) -> Optional[Node]:
    """Search for a value and return its node or ``None``.

    :param value: The integer value to search for.
    :return: The matching Node or None if not found.
    :raises TypeError: If the search value is not an integer.
    """
    if not isinstance(value, int):
      raise TypeError("The search value must be an integer.")
    return self._search_recursive(self.root, value)

  def _search_recursive(self, current: Optional[Node], value: int) -> Optional[Node]:
    """Recursively traverse the tree discarding inapplicable subtrees.

    :param current: The currently inspected node.
    :param value: The target search value.
    :return: The matching Node or None.
    """
    if current is None or current.value == value:
      return current

    if value < current.value:
      return self._search_recursive(current.left, value)
    return self._search_recursive(current.right, value)

  def contains(self, value: int) -> bool:
    """Check if a value exists in the tree.

    :param value: The value to verify.
    :return: True if the value is present, otherwise False.
    """
    return self.search(value) is not None

  # =========================================================================
  # DELETION
  # =========================================================================
  def delete(self, value: int) -> None:
    """Remove an integer value from the tree if present.

    :param value: The integer value to delete.
    :raises TypeError: If the value to delete is not an integer.
    """
    if not isinstance(value, int):
      raise TypeError("The value to delete must be an integer.")
    self.root = self._delete_recursive(self.root, value)

  def _delete_recursive(self, current: Optional[Node], value: int) -> Optional[Node]:
    """Recursively delete a value and update the subtree structure.

    :param current: The root node of the current subtree.
    :param value: The value to delete.
    :return: The updated root node of the subtree after deletion.
    """
    if current is None:
      return None

    # Navigate toward the target node
    if value < current.value:
      current.left = self._delete_recursive(current.left, value)
    elif value > current.value:
      current.right = self._delete_recursive(current.right, value)
    else:
      # Found the target node to delete

      # Case 1: Node has no children (leaf node)
      if current.left is None and current.right is None:
        return None

      # Case 2: Node has exactly one child
      if current.left is None:
        return current.right
      elif current.right is None:
        return current.left

      # Case 3: Node has two children
      # Find the in-order successor (smallest value in the right subtree)
      successor = self._get_minimum(current.right)
      current.value = successor.value
      # Remove the successor node from the right subtree
      current.right = self._delete_recursive(current.right, successor.value)

    return current

  def _get_minimum(self, node: Node) -> Node:
    """Retrieve the node with the minimum value in a subtree.

    :param node: The root node of the subtree to search.
    :return: The node with the smallest value.
    """
    current = node
    while current.left is not None:
      current = current.left
    return current

  # =========================================================================
  # IN-ORDER TRAVERSAL
  # =========================================================================
  def inorder(self) -> List[int]:
    """Return all tree values in ascending order.

    :return: Sorted list of all integer values.
    """
    elements: List[int] = []
    self._inorder_recursive(self.root, elements)
    return elements

  def _inorder_recursive(
    self, current: Optional[Node], elements: List[int]
  ) -> None:
    """Recursively append values in left-root-right order.

    :param current: The currently visited node.
    :param elements: Destination list for sorted values.
    """
    if current is not None:
      self._inorder_recursive(current.left, elements)
      elements.append(current.value)
      self._inorder_recursive(current.right, elements)


# =============================================================================
# USAGE EXAMPLE AND TESTS
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

# 1. Brute Force Approach
def two_sum_brute_force(arr, target):
    """
    Brute force approach to find two elements in array that sum to target.
    Time Complexity: O(n^2)

    Args:
        arr (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int] or None: Pair of numbers that sum to target, or None if not found.
    """
    n = len(arr)
    for i in range(n):
        b = target - arr[i]
        for j in range(i + 1, n):
            if arr[j] == b:
                return [arr[i], b]
    return None

# 2. Binary Search Tree Approach


class TreeNode:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, idx):
        def _insert(node, val, idx):
            if not node:
                return TreeNode(val, idx)
            if val < node.val:
                node.left = _insert(node.left, val, idx)
            else:
                node.right = _insert(node.right, val, idx)
            return node
        self.root = _insert(self.root, val, idx)

    def find(self, val):
        def _find(node, val):
            if not node:
                return -1
            if node.val == val:
                return node.idx
            elif val < node.val:
                return _find(node.left, val)
            else:
                return _find(node.right, val)
        return _find(self.root, val)


def two_sum_bst(arr, target):
    """
    Binary Search Tree based approach to two sum problem.
    Time Complexity: O(n log n)

    Args:
        arr (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int] or None: Pair of numbers that sum to target, or None if not found.
    """
    tree = BST()
    for i, val in enumerate(arr):
        tree.insert(val, i)
    for i, val in enumerate(arr):
        b = target - val
        j = tree.find(b)
        if j != -1 and i != j:
            return [val, b]
    return None

# 3. Hash Map Approach


def two_sum_hashmap(arr, target):
    """
    Hash map approach to find two elements in array that sum to target.
    Time Complexity: O(n)

    Args:
        arr (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[int] or None: Pair of numbers that sum to target, or None if not found.
    """
    value_to_index = {}
    for i, val in enumerate(arr):
        b = target - val
        if b in value_to_index:
            return [val, b]
        value_to_index[val] = i
    return None

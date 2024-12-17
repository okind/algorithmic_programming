import unittest
from rotate_linked_list import ListUtils, ListNode

# write unit tests


class TestRotateLinkedList(unittest.TestCase):
    sut = ListUtils()

    def create_linked_list(self, values):
        """Helper function to create a linked list from a list of values"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """Helper function to convert linked list to regular list for comparison"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_empty_list(self):
        """Test rotating an empty list"""
        self.assertIsNone(self.sut.rotateRight(None, 5))

    def test_single_node(self):
        """Test rotating a list with single node"""
        head = self.create_linked_list([1])
        rotated = self.sut.rotateRight(head, 3)
        self.assertEqual(self.linked_list_to_list(rotated), [1])

    def test_zero_rotation(self):
        """Test with k = 0 (no rotation)"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        rotated = self.sut.rotateRight(head, 0)
        self.assertEqual(self.linked_list_to_list(rotated), [1, 2, 3, 4, 5])

    def test_normal_rotation(self):
        """Test normal case with k < length"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        rotated = self.sut.rotateRight(head, 2)
        self.assertEqual(self.linked_list_to_list(rotated), [4, 5, 1, 2, 3])

    def test_large_k(self):
        """Test with k > length"""
        head = self.create_linked_list([1, 2, 3])
        rotated = self.sut.rotateRight(head, 5)
        self.assertEqual(self.linked_list_to_list(rotated), [2, 3, 1])

    def test_k_equals_length(self):
        """Test with k = length (should be same as original)"""
        head = self.create_linked_list([1, 2, 3, 4])
        rotated = self.sut.rotateRight(head, 4)
        self.assertEqual(self.linked_list_to_list(rotated), [1, 2, 3, 4])

    def test_two_nodes(self):
        """Test with two nodes for different k values"""
        head = self.create_linked_list([1, 2])
        rotated = self.sut.rotateRight(head, 1)
        self.assertEqual(self.linked_list_to_list(rotated), [2, 1])

    def test_cycle_detection(self):
        """Test that the rotation doesn't create unintended cycles"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        rotated = self.sut.rotateRight(head, 2)
        # Check if last node points to None
        current = rotated
        while current.next:
            current = current.next
        self.assertIsNone(current.next)


if __name__ == '__main__':
    unittest.main()

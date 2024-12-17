''' 
PROBLEM DESCRIPTION
rotate the linked list to the right by k positions.

input [1,2,3,4,5] k=2 
output [4,5,1,2,3]

the number of nodes in the list [0,500] - small size of data
k - number of rotations, 0<=k<=2*10^9 - large size

SOLUTION

Rotating a list involves cyclically shifting the elements' positions by one to the right.
Algorithm steps:
1. Initial checks: if list is empty, has only one element or number of rotations given is 0.
 This checks prevent unncessary processing. Return original list.
2. Traverse the list to count nodes and find the last node, the tail of the linked list.
 It is O(n) time complexity
3. Normalize k to reduce unnecessary rotations
    The modulo operator (%) gives us the remainder after division.
    Since the list returns to its original state after 'length' rotations
    Any additional rotations beyond 'length' are redundant.
    k % length gives us the minimal number of rotations needed. 
4. Find the breakpoint
 Move k % lenght steps from the head. The next node will become our new head.
5. Perform rotation
   Set the new head, node after breakpoint.
   Connect last node, tail to the original head.
   Return new head.
'''

# Definition for singly-linked list.
# The ListNode class represents a node in a singly linked list.
# It is a basic building block for creating and working with linked lists in Python.


class ListNode:
    # Initializes a node with a value (val) and a pointer to the next node (next).
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListUtils(object):
    # The method takes two inputs: head: The head of a singly linked list.
    # k: The number of positions to rotate the list to the right.
    def rotateRight(self, head: ListNode, k):
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        rotations_num = k % length
        if rotations_num == 0:
            return head

        # Separate at breakpoint and set a new head
        breakpoint = head
        for i in range(length - rotations_num - 1):
            breakpoint = breakpoint.next
        new_head = breakpoint.next
        breakpoint.next = None

        # Point tail to head
        tail.next = head
        return new_head

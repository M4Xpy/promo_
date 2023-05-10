"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if head or head.next or k:
            tail = head
            length = 1
            while tail.next:
                tail = tail.next
                length += 1
            tail.next = head  # Circle the list

            t = length - k % length
            for _ in range(t):
                tail = tail.next
            newHead = tail.next
            tail.next = None

            return newHead
        return head




class TestSearchInsert:

    def test_solo(self):
        assert Solution().rotateRight(head=[1, 2, 3, 4, 5], k=2
                                      ) == [4, 5, 1, 2, 3]

    # def test_k_more_than_head(self):
    #     assert Solution().rotateRight(head=[0, 1, 2], k=4
    #                                   ) == [2, 0, 1]
#
#     def test_solo(self):
#         assert Solution().xxxxx(  xxxx
#                                  ) == xxx

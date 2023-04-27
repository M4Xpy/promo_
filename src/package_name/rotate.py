"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        k %= len(head)
        return head[-k:] + head[:-k]


class TestSearchInsert:

    def test_solo(self):
        assert Solution().rotateRight(head=[1, 2, 3, 4, 5], k=2
                                      ) == [4, 5, 1, 2, 3]

    def test_k_more_than_head(self):
        assert Solution().rotateRight(head=[0, 1, 2], k=4
                                      ) == [2, 0, 1]
#
#     def test_solo(self):
#         assert Solution().xxxxx(  xxxx
#                                  ) == xxx

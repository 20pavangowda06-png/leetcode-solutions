"""
LeetCode 206 - Reverse Linked List (Easy, bonus problem)
https://leetcode.com/problems/reverse-linked-list/

Local test harness included below. When submitting to LeetCode,
paste ONLY the Solution class - LeetCode already provides ListNode.
"""
from typing import Optional


class ListNode:
    """Defined here for local testing; the judge provides its own."""
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ===== LEETCODE SOLUTION START =====
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next  # save before overwriting
            curr.next = prev  # flip the link
            prev = curr
            curr = nxt
        return prev  # prev ends up at the new head
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
def make_list(vals: list[int]) -> Optional[ListNode]:
    head = tail = None
    for v in vals:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "1 typical"),
        ([7], [7], "2 edge (single node)"),
        ([], [], "3 edge (empty list)"),
    ]
    passed = True
    for given, expected, label in cases:
        got = to_list(sol.reverseList(make_list(given)))
        ok = got == expected
        print(f"Test {label}: {got} "
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

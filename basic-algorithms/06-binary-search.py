"""
LeetCode 704 - Binary Search (Easy)
https://leetcode.com/problems/binary-search/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4, "1 typical (found)"),
        ([-1, 0, 3, 5, 9, 12], 2, -1, "2 typical (not found)"),
        ([5], 5, 0, "3 edge (single element, found)"),
        ([5], 3, -1, "4 edge (single element, not found)"),
        ([], 1, -1, "5 edge (empty array)"),
    ]
    passed = True
    for nums, target, expected, label in cases:
        got = sol.search(nums, target)
        ok = got == expected
        print(f"Test {label}: target {target} -> index {got} "
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

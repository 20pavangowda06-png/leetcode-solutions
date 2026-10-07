"""
LeetCode 283 - Move Zeroes (Easy)
https://leetcode.com/problems/move-zeroes/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # `w` marks where the next non-zero element belongs; everything
        # before `w` is already a non-zero in original relative order.
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0], "1 typical"),
        ([0, 0, 0], [0, 0, 0], "2 edge (all zeroes)"),
        ([1, 2, 3], [1, 2, 3], "3 edge (no zeroes)"),
        ([0], [0], "4 edge (single zero)"),
    ]
    passed = True
    for given, expected, label in cases:
        buf = list(given)
        sol.moveZeroes(buf)
        ok = buf == expected
        print(f"Test {label}: {buf} "
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

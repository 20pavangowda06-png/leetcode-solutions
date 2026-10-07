"""
LeetCode 1 - Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:          # complement seen before -> done
                return [seen[need], i]
            # store AFTER lookup so we never pair an element with itself
            seen[x] = i
        return []  # unreachable per problem guarantee
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases (duplicates, negatives).
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([2, 7, 11, 15], 9, [0, 1], "1 typical"),
        ([3, 2, 4], 6, [1, 2], "2 edge (duplicate values)"),
        ([-3, 4, 3, 90], 0, [0, 2], "3 edge (negatives)"),
    ]
    passed = True
    for nums, target, expected, label in cases:
        got = sol.twoSum(nums, target)
        ok = got == expected
        print(f"Test {label}: target {target} -> {got} "
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

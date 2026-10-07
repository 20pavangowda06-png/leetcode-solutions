"""
LeetCode 242 - Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # quick reject
        counts: dict[str, int] = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1
            if counts[ch] < 0:
                return False  # early exit on surplus char
        return True
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("anagram", "nagaram", True, "1 typical"),
        ("rat", "car", False, "2 typical (not anagram)"),
        ("a", "ab", False, "3 edge (different lengths)"),
        ("", "", True, "4 edge (both empty)"),
        ("aacc", "ccac", False, "5 edge (same length, different counts)"),
    ]
    passed = True
    for s, t, expected, label in cases:
        got = sol.isAnagram(s, t)
        ok = got == expected
        print(f'Test {label}: ("{s}","{t}") -> {got} '
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

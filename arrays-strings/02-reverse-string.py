"""
LeetCode 344 - Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("hello", "olleh", "1 typical"),
        ("a", "a", "2 edge (single char)"),
        ("", "", "3 edge (empty string)"),
        ("ab", "ba", "4 edge (even length)"),
    ]
    passed = True
    for given, expected, label in cases:
        buf = list(given)
        sol.reverseString(buf)
        got = "".join(buf)
        ok = got == expected
        print(f'Test {label}: "{given}" -> "{got}" '
              f'(expected "{expected}"): {"PASS" if ok else "FAIL"}')
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

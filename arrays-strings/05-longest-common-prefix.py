"""
LeetCode 14 - Longest Common Prefix (Easy)
https://leetcode.com/problems/longest-common-prefix/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        # Grow the prefix one character at a time while every string matches.
        prefix: list[str] = []
        for i, ch in enumerate(strs[0]):  # first string is the reference
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return "".join(prefix)
            prefix.append(ch)
        return "".join(prefix)
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        (["flower", "flow", "flight"], "fl", "1 typical"),
        (["dog", "racecar", "car"], "", "2 typical (no common prefix)"),
        (["a"], "a", "3 edge (single string)"),
        (["ab", "a"], "a", "4 edge (one string is a prefix of another)"),
        ([""], "", "5 edge (empty string)"),
        ([], "", "6 edge (no strings)"),
    ]
    passed = True
    for strs, expected, label in cases:
        got = sol.longestCommonPrefix(strs)
        ok = got == expected
        print(f'Test {label}: "{got}" '
              f'(expected "{expected}"): {"PASS" if ok else "FAIL"}')
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

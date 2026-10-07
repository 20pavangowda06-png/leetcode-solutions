"""
LeetCode 20 - Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        pairs = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in "([{":
                stack.append(ch)  # push opener
            elif not stack or stack.pop() != pairs[ch]:
                return False     # closer with no matching opener
        return not stack         # every opener must be closed
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("()[]{}", True, "1 typical"),
        ("(]", False, "2 typical (mismatched)"),
        ("([)]", False, "3 edge (interleaved, not properly nested)"),
        ("", True, "4 edge (empty string)"),
        ("((()))", True, "5 edge (deep nesting)"),
        (")", False, "6 edge (lone closer)"),
    ]
    passed = True
    for s, expected, label in cases:
        got = sol.isValid(s)
        ok = got == expected
        print(f'Test {label}: "{s}" -> {got} '
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

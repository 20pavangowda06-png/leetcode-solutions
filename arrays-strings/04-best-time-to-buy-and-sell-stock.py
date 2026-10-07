"""
LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Local test harness included below. When submitting to LeetCode,
paste only the section between SOLUTION START / SOLUTION END.
"""

# ===== LEETCODE SOLUTION START =====
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]  # cheapest buy day seen so far
        best = 0               # best profit seen so far
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best
# ===== LEETCODE SOLUTION END =====


# Local tests: one typical case, plus edge cases.
if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([7, 1, 5, 3, 6, 4], 5, "1 typical"),
        ([7, 6, 4, 3, 1], 0, "2 edge (always falling -> no trade)"),
        ([1], 0, "3 edge (single day)"),
        ([2, 4, 1], 2, "4 edge (best deal is early)"),
        ([], 0, "5 edge (empty)"),
    ]
    passed = True
    for prices, expected, label in cases:
        got = sol.maxProfit(prices)
        ok = got == expected
        print(f"Test {label}: profit {got} "
              f"(expected {expected}): {'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")

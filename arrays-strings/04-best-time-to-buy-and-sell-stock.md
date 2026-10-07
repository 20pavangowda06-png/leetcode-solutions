## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
One pass through the prices, tracking the cheapest price seen so far and the best profit achievable. For each new day, either it's a new cheapest buy day (update `minPrice`) or selling today beats the previous best (update `best`). The key insight is that the optimal sell day for any buy day is simply the maximum price after it, so remembering only the minimum so far is enough.

### Complexity
- Time: O(n) — single pass
- Space: O(1) — two variables

### Notes
- Edge case: prices that only fall (e.g. `[7,6,4,3,1]`) give profit 0 — you just don't trade. The `best` starting at 0 handles this.
- This is the one-transaction version. The "as many transactions as you like" variant (LeetCode 122) is a natural next step.
- Local tests: typical case, falling prices, single day, best deal early in the array.

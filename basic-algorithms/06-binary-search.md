## Problem: Binary Search (Easy)
**Link:** https://leetcode.com/problems/binary-search/

### Approach
Classic iterative binary search on a sorted array: keep a `[lo, hi]` window, check the midpoint, and discard the half that can't contain the target. The midpoint is computed as `lo + (hi - lo) / 2` instead of `(lo + hi) / 2` to avoid integer overflow on large arrays — a detail interviewers love to ask about.

### Complexity
- Time: O(log n) — the search space halves each step
- Space: O(1) — iterative, no recursion stack

### Notes
- Edge cases: empty array returns -1 immediately since `hi = -1 < lo = 0`; single-element arrays work through the normal path.
- The loop invariant to remember: if the target is present, it is always within `[lo, hi]`. Every update preserves this.
- Local tests: found, not found, single element (found/not found), empty array.

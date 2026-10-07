## Problem: Move Zeroes (Easy)
**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
Two pointers in a single pass: a read pointer `r` scans every element, and a write pointer `w` marks where the next non-zero belongs. Each non-zero found is swapped into position `w`, so all non-zeroes keep their original relative order and the tail fills with zeroes. In-place, one pass.

### Complexity
- Time: O(n) — one pass
- Space: O(1) — in place

### Notes
- Edge cases: all zeroes (nothing moves, `w` stays 0), no zeroes (every element swaps with itself — harmless), single zero.
- The "keep relative order" requirement is what rules out a simple partition; the two-pointer write index is the standard trick for stable in-place rearrangement.
- Local tests: typical case, all zeroes, no zeroes, single zero.

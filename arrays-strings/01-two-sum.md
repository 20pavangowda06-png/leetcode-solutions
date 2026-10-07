## Problem: Two Sum (Easy)
**Link:** https://leetcode.com/problems/two-sum/

### Approach
For each number, I check whether its complement (`target - x`) has been seen before, using a dict from value to index — O(1) average lookup. Storing each element *after* the lookup guarantees I never pair an element with itself, which is what makes the duplicate-value case like `[3, 3]` with target `6` work correctly.

### Complexity
- Time: O(n) average — one pass, one dict lookup/insert per element
- Space: O(n) — the dict stores up to n entries

### Notes
- Edge case learned: with duplicates, insert-after-lookup ordering matters. Inserting first would let `3` match itself.
- A cleaner alternative for interviews: sort a copy with original indices and use two pointers — O(n log n) time, O(n) space, no hash table needed.
- Local tests: typical case, duplicate values, negative numbers.

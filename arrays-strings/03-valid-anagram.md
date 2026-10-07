## Problem: Valid Anagram (Easy)
**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
Count character frequencies of the first string in a dict, then decrement while scanning the second string. If any count goes negative, the strings can't be anagrams — this gives an early exit without a final verification loop. A length check up front rejects mismatched strings immediately.

### Complexity
- Time: O(n) — two linear scans
- Space: O(k) — the dict holds at most k distinct characters (k ≤ n)

### Notes
- The one-liner `collections.Counter(s) == collections.Counter(t)` works too, but the manual version shows the technique and exits early on a mismatch.
- Follow-up worth knowing: "what if the inputs are huge and streamed?" — same counting idea, just process in chunks.
- Local tests: true anagram, non-anagram, different lengths, both empty, same length with different counts.

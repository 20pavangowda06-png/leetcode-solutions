## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
Grow the prefix one character at a time: take the next character of the first string and check it against the same position in every other string. The moment any string differs (or ends), the prefix is complete. Using the first string as the reference keeps the code simple and avoids sorting.

### Complexity
- Time: O(S) where S is the total number of characters examined — at most the full input in the worst case
- Space: O(1) extra besides the returned string (O(m) for the result itself, where m is the prefix length)

### Notes
- Edge cases: a single string returns itself; an empty string anywhere forces the answer to `""`.
- Alternative approach: sort the array and only compare the first and last strings — the common prefix of the extremes is the common prefix of all. Same complexity, arguably cleaner.
- Local tests: typical case, no common prefix, single string, one string being a prefix of another, empty string.

## Problem: Reverse String (Easy)
**Link:** https://leetcode.com/problems/reverse-string/

### Approach
Two pointers, one starting at each end of the array, swapping characters and walking toward the middle. This reverses the string in place with no extra allocation, which is exactly what the problem asks for (O(1) extra memory).

### Complexity
- Time: O(n) — each pair is swapped once
- Space: O(1) — only the temporary swap variable

### Notes
- Edge cases: empty string and single character need no swaps; the `left < right` loop condition handles both naturally.
- This two-pointer pattern shows up everywhere (palindromes, reversing linked lists), so it's worth knowing cold.
- Local tests: typical "hello", single char, empty string, even-length string.

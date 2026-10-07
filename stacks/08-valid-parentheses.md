## Problem: Valid Parentheses (Easy)
**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach
Scan left to right with a stack: push every opening bracket, and on each closing bracket pop the top and check it matches. Three failure modes return false early — a closer with an empty stack, a mismatched pair, and (at the end) leftover openers on the stack. The stack depth never exceeds the input length, so a fixed buffer works.

### Complexity
- Time: O(n) — each character is pushed/popped at most once
- Space: O(n) — the stack in the worst case (e.g. `"(((((("`)

### Notes
- Edge case learned: `"([)]"` is invalid despite having balanced counts — nesting order matters, which is exactly why a stack (LIFO) is the right structure and counting isn't enough.
- A Python list works perfectly as a stack (`append`/`pop`); no fixed-size buffer needed.
- Local tests: valid mix, mismatched pair, interleaved brackets, empty string, deep nesting, lone closer.

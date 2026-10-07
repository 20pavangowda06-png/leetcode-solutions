## Problem: Reverse Linked List (Easy) — bonus
**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
Iterative pointer reversal: walk the list with `curr`, keeping `prev` as the already-reversed prefix. At each step, save `curr->next` first (otherwise the rest of the list is lost), point `curr->next` back at `prev`, then advance both pointers. When `curr` hits NULL, `prev` is the new head.

### Complexity
- Time: O(n) — one pass
- Space: O(1) — three pointers

### Notes
- The critical detail: save `next` *before* overwriting `curr->next`. Forgetting this is the classic bug — the list gets truncated.
- Edge cases: empty list returns NULL, single node returns itself — both fall out of the loop naturally.
- Recursive version exists (elegant but O(n) stack space); iterative is preferred here.
- Note for LeetCode submission: paste only the `Solution` class — the `ListNode` class is provided by the judge. It's defined here so the file runs locally.
- Local tests: 5-node list, single node, empty list.

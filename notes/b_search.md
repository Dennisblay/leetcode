# Binary Search

Binary search is an algorithm for searching a sorted list or an array.
It operates by continuously partitioning the array in half and determining which half has the target item and
discarding or filtering out the other half which doesn't.

## Runtime

- Intuitively, BS search is often faster than linear scans.
- It actually depends on the data and the target item.
- Linear scan would obviously win if the target item is at the start of the list and would take forever if the item is
  at the bottom or end or if it isn't in the list at all.
- We don't need to partition a list in half if the list has only 2 elements.
- Linear scan: O(n)
- Binary search: O(log **2** N)
- At the end of the day, we care about the performance of the algorithm when the data grows, so the logarithmic number
  of comparisons will far outweighs the further additional code complexity.  
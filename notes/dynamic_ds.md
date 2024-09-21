# Dynamic Data Structures

## Linked Lists

- Unlike arrays, linked lists are dynamic and they're layout in memory isn't as fixed and contiguous as arrays are.
- Their locations in memory are scattered.
- It is a chain of nodes, where each node, which is usually a composite type, contains the value it contains and a
  pointer or reference to the next node in the list.
- Because they include pointers as well as values, they require more memory than arrays to store the same items.
- If we have an array of size K, storing values of N bytes each, we only need

 ```
  K × N bytes.
  ```

- With linked lists, we would need

 ```
K * ( N + P )
```

- However, the increased memory usage is often worth it for the increased flexibility
  the pointers provide.
- There's a trade-off between flexibility and speed of retrieval or indexing.
- It takes only one mathematical computation to compute a single offset and a single memory lookup with arrays.
- However with linked lists, the list would require us to iterate from the beginning of the list to get to the destination.  
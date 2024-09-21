# Complexity Analysis,

## Asymptotic Analysis & Big O

- The behaviour or runtime of an algorithm in terms of time and space as the input data grows.
- Eg:
- ```
  F(n) = 10n + 1
  ```
- As n, which is the input grows or becomes very large or approaches infinity, what is the behaviour of F(n), the
  output.
- The number of operations F(n) performs or the number of steps taken is studied in asymptotic analysis.
- Interested in the function, F(n) when n grows.
- In asymptotic analysis, we are only interested in the trend and not the specifics of the details as well as the upper
  bound or the worse case scenario of the input data.
- For instance, in

 ```
F(n) = 10n + 1
```

- We use the Big O notation to denote or express the asymptotic analysis and the time complexity of an algorithm in
  general. In this case, we can ignore the constants and conclude that the function is of the Order n, or has a time
  complexity of Order n...:

 ```
O(n)
```

- Which reads as, the operation is bounded by a multiple of n, Or, as the i/p size increases, the time taken increases
  linearly or the number of operations scales or grows proportionally with n.

- The value `1` becomes insignificant when n grows up to say 1 billion.

## Logarithm

- An algorithm is denoted to have an `O(logN)` if at every set or operation, it partitions it's I/p data in half.eg.
  Binary search
- It is said to scale `logarithmically` with the I/p data.
- The result the asymptotic analysis is simple the number of operations or steps taken to run an algorithm in time
  complexity.
- For example, in a binary search algorithm with an I/p size of `N=16` has an `O(log16)`. Which is the result of
  `2^? = 16`, which is `4`. 
- It interprets as, 4 operations are required in the algorithm in every step.  
- **Tip**: If the I/P data is doubled, one extra operation is required.

### Keywords

- Growth rate
- Asymptotic
- scales, grows
- proportional
- time and space complexity
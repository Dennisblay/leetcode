# Recursion

A recursive function is one that calls itself until a base condition is met.
When a solving a sub-problem solves the original problem.

eg:

```python
def out(num: int):
    if num > 10:
        return
    print(num)
    out(num + 1)
```

## Steps leap of faith

- Understand the problem.
- Identify the sub-problem.
- Leap of faith/trust.
- Link sub-problem and original problem.
- Base condition

eg:

```python
def out(num: int):
    if num <= 0:  # Label: base case check
        return
    print(num)  # Label: print before recursion
    out(num - 1)  # Label: recursive call, also inductive case, if it works for n, it will work for (n-1) 
    print(num)  # Label: print after recursion
```

- The `function definition` (see `# Label: function definition`) defines the `out` function, which is the main recursive
  function.
- Before each recursive call, the function prints the current value of `num` (`# Label: print before recursion`).

In visualising recursion, two methods are powerful mostly used

- Recursion Tree
    - Visualize fn calls in the form of trees
- Recursion Call Stack
    - Computer allocates memory for fn calls

## Recursion vs Iteration

- Things done recursively can also be done iteratively.
- The iterative approach does not use recursive call stack.
- So can achieve a better space complexity with the iterative approach than we can with the recursion.
- Additionally, recursion has two phases;
    - The ascending phase
    - The descending phase
- Iteration has only the ascending phase (There's no coming or looking back).
- while iteration can save up some space, recursion has better readability and ease of implementation of complex
  problems

```
LIFO - Last in First out 
___________________________
f(1)|  - base condition will be met here
print(1)
f(2)|
print(2)
f(3)|
print(3)
f(4)|
print(4)
f(5)|
print(5)
```

### Ways to write Base Condition

- To identify the base condition, don't try to visualize the whole recursive sequence, but look at:
    - The first invalid input or
    - The Last valid input

### Recurrence Relation

- Expression of the solution to the original problem as a function of the solutions to smaller instances of the same
  problem.
- Talks about the solution to the sub-problem.
  eg. For finding the `n` factorial

 ```
F(n) = F(n - 1) * n
```

## Complexity and Analysis of Recursive Solutions

- Time complexity = #Nodes x [Work done per node]
- Space complexity = maximum depth of Tree or recursive call stack
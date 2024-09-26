# Backtracking

- Backtracking in general means retracing the steps that you have just followed.
- In algorithmic speak, backtracking is an algorithmic approach to finding solutions to problems that involve many
  possible paths.
- Controlled recursion with the state of the problem changed in place by pass by reference.
- Solution is built step by step using **recursion**.
- Backtracking is controlled recursion - if a path does not lead to the solution or violates constraints, it is
  abandoned.
- Changes of the solution to the problems are made in place (by pass by reference)
- Copies are not made.
- Better space complexity because we are not creating any additional space.
- BTracking algorithms are a type of brute force solution (pure recursion)
- Except, wrong paths are pruned if condition or
  constraint is violated until the correct solutions are found.
- Unlike in pure recursion, where all possible paths will be considered before checking which paths are the correct
  paths.
- we only explore paths that leads to a solution and end up with the correct solutions.

## When to use Backtracking

- When problem requires multiple solutions (not always the case as in sodoku, where only one path is the (correct)
  solution).
- Not suitable for the optimized solution.
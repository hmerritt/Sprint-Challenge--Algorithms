#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) __O(n)__ - As n increases so does the operations in a linear fashion (n * n * n) / (n * n) = n


b) __O(n log n)__ - for loop += n. while loop will increase as n does since j = 1 and it checks for j < n. But j * 2 each time which is an exponential increase each iteration so it can't be n^2 but rather n log n


c) __O(n) : O(n * 2)__ - bunnyEars recursively runs from n down to 0 (never any more) making the operations performed proportionate to n

## Exercise II

Binary search algorithm.

Try dropping an egg off half of n;
- if it breaks then half the height and try again

- if not then use the top half ((n / 2) + (n / 4) this time) and try again

Repeat until you find the highest non breaking-point.

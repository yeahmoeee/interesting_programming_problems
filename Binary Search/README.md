# Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

## Example Test Case

```rb
binary_search(nums = [-1,0,3,5,9,12], target = 9) -> 4

binary_search(nums = [-1,0,3,5,9,12], target = 2) -> -1
```

## Approach

Since the question is asking us to write an algorithm in O(log n), the first thing that should come into your mind is some kind of algorithm that shrink the search space by half through each iteration.

Binary search is a popular searching algoritm to find the target value in a sorted array. The general idea is that we make comparison of target value with the middle value of the current search space, and shrink the search space by approximately half in each iteration accordingly. 

1st Iteration: n elements 

2nd Iteration: n/2 elements

3rd Iteration: n/4 elements

...

(log N)th Iteration: 1 elements

There are at most log n iterations to find the target.


### Algorithm:
1. Create a pointer variable "l","r" and "mid" and store 0, last index and 0 respectively.

2. Use a while loop with the condition (l <= r). 
   * Set "mid" to be (l + r)//2 
   * Check condition:
      * If the value at "mid" is equal to the target value, then simply return "mid".
      * If the value at "mid" is less than the target value, then set "l" to (mid - 1).
      * If the value at "mid" is greater than the target value, then set "r" to (mid + 1).
3.  After jumping out of while loop, return -1 since target cannot be found.

### Analysis:
If there are n elements in the list, there are at most log n iterations, so in the worst case scenario, it is O(log n) in time complexity. Since only a few variables are defined, it is O(1) in space complexity. 








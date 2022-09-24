# Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


## Example Test Case

```rb
searchInsert(nums = [1,3,5,6], target = 5) -> 2 

searchInsert(nums = [1,3,5,6], target = 2) -> 1

searchInsert(nums = [1,3,5,6], target = 7) -> 4

```

## Approach

Since the question is asking us to write an algorithm in O(log n), the first thing that should come into your mind is some kind of algorithm that shrink the search space by half through each iteration. 

As you can see, since the array is sorted, we use [Binary Search](https://github.com/yeahmoeee/interesting_programming_problems/tree/main/Binary%20Search) to look for the index. If the target is not found, then return the index which the target should be inserted in. 


### Algorithm:
1. Create a pointer variable "l" and "r" and store 0 and last index.

2. Use a while loop with the condition (l <= r). 
      - Create a variable "mid" to be (l + r)//2 
      - Check condition:
            -If the value at "mid" is equal to the target value, then simply return "mid".
            -If the value at "mid" is less than the target value, then
            set "l" to (mid - 1).
            -If the value at "mid" is greater than the target value, then
            set "r" to (mid + 1).
3.  After jumping out of while loop, return "l".

### Analysis:

If there are n elements in the list, there are at most log n iterations, so in the worst case scenario, it is O(log n) in time complexity. Since only a few variables are defined, it is O(1) in space complexity. 



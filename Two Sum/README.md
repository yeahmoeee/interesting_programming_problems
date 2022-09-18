# Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


## Example Test Case

```rb
twoSum(nums = [2,7,11,15], target = 9)  -> [0,1] 

twoSum(nums = [3,2,4], target = 6)      -> [1,2]

twoSum(nums = [3,3], target = 6)        -> [0,1]

```

## Approach

The naive approach to this question is to use double for-loop. That would be O(n^2) in time complexity and O(1) in space complexity. This approach basically enumerate all possible distinct pairs of number in the worst case.

An improvement to this approach would be to utilize hash map. We starts by initializing an empty hash map. We then iterate through the list. As we go along, we check if the target value minus the current value in the iteration is present in the hash map, if it is, then we return the corresponding index, else we add the current value as key to the dictionary with its index as the value.


### Algorithm:
1. Initialize an empty hash map "dict_".

2. Iterate through "nums"
        -If the target value minus the current value is present in dict_, then we return [current index,dict_[target value minus the current value]]
        -Else, we add current value as key to the dictionary with its index as the value.

### Analysis:
Suppose that the list has n elements, then it is O(n) in time complexity since we are iterating the list with just one for loop, but it is O(n) in space complexity as well since a hash map is utlized to stored the key-value pair of every elements in the worst case.





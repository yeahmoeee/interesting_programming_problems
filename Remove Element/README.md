# Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.




## Example Test Case

```rb
removeElement(nums = [3,2,2,3], val = 3)          -> 2, nums = [2,2,_,_]

removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)  -> 5, nums = [0,1,4,0,3,_,_,_]
```

## Approach

A easy approach to this question would be to create another array to store the value that isn't equal to "val" as you iterate through "nums", but since we aren't allowed to allocate any extra memory for another array, we have to do it in-place instead.

In order to do in-place removal, as you iterate through "nums", check if the value is equal to "val", if it is, then do nothing, else, then set "nums" at index "i" (initially set to 0) to the value and then increment "i" by 1. In the end, simply return "i" as it contains the length of the array after removing all occurences of "val".


### Algorithm:
1. Set variable "i" to 0.
2. Iterate through "nums"
        -If the value is equal to "val", then do nothing.
        -Else, set "nums" at index "i" to the value and then increment "i" by 1.
3. Return "i".

### Analysis:
Since we are iterating through the entire array, this is O(n) in time complexity both at best and worst case scenario. We are doing the removal in-place, so no extra memory is allocated for any extra array, thus this is O(1) in space complexity.


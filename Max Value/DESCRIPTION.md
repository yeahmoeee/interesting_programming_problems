# Max Value

Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.

Solve this without using any built-in list methods.

You can assume that the list is non-empty.

## Example Test Case

max_value([1,2,3,4,5]) -> 5
max_value([3,4,7,5])   -> 7

## Approach

You can used built-in max() function to solve this problem. 

Since you need to iterate over all the elements in the list to find the max value, the time and space complexity is O(n) and O(1) respectively.

You could sort the list in reverse order and return the first element in the array. But it is not efficient, the time complexity is at best O(nlogn) and space complexity is at best O(1).

The most efficient approach for finding the max value is to iterate through the list and make comparison throughout. 

Algorithm:
1. Create a dummy variable "max_value" and set it to the smallest number possible in your programming language. 

2. Iterate through the list, and do comparison with the variable "max_value", if the value is greater than "max_value", then replace "max_value" with the value, else continue. 

3. Eventually, "max_value" is stored with the largest value in the list. Simply just return the variable.

Analysis:
If there are n elements in the list, there are at most n comparisons, so in the worst case scenario, it is O(n) in time complexity. Since only one variable is defined, it is O(1) in space complexity. 








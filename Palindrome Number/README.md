# Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


## Example Test Case

```rb
isPalindrome(121) -> True

isPalindrome(-121) -> False
```

## Approach

If the integer is negative, then we can simply just return false since it cannot be a palindrome with the minus sign. 

Otherwise, we can cast the integer into string, and check if the reversal of that string is equal to itself, if it is, return true else false.

If you don't like the idea of casting, then you could store each digits of the integer in a list by iterating the integer over a while loop, and do the final checking.


### Algorithm:
1. If the integer is less than zero, then return False.

2. Cast the integer into string and stored the result in "x". 

3. Check if the reversal of that string is equal to itself. Return True if it is, else return False.

### Analysis:
Suppose the integer is n digits long, then both casting and reversal is O(n) in time complexity. If you used any kind of list or array, then it is O(n) in space complexity, but since we didn't used any, it is O(1) in space complexity.



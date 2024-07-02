#9. Palindrome Number

#Runtime
# 26 ms
# Beats 95.57%
# Analyze Complexity
# Memory
# 11.39 MB
# Beats 98.32%

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints: -231 <= x <= 231 - 1

#Solution:

class Solution(object):
    def isPalindrome(self, x):
        num=str(x)
        if(x>=0):#if negative return false as it is already
            num_rev = num[::-1]
            if num == num_rev:
                return True
        
        return False
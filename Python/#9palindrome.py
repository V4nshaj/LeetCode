#9. Palindrome Number
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
        num_rev=''
        i=len(num)-1
        if(x<0):#if negative return false as it is already
            return False
        else:
            while i>=0:
                num_rev =num_rev+num[i]
                i=i-1
            if num == num_rev:
                return True
                
            else:
                return False
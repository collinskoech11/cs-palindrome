"""
Valid Palindrome:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
#Binary Search Solution
class Solution:
    def isPalindrome(self, s:):
        y = str(s)
        a_pointer,b_pointer  = 0, len(y) - 1

        while a_pointer < b_pointer:

            while a_pointer < b_pointer and not y[a_pointer].isalnum():
                a_pointer += 1
            while a_pointer < b_pointer and not y[b_pointer].isalnum():
                b_pointer -= 1

            if s[a_pointer].lower() != y[b_pointer].lower():
                return False

            a_pointer += 1
            b_pointer -= 1

        return True
    
    #Second Solution 
    class Solution:
        def isPalindrome(self, s):
            y = str(s)
            x  = s.reverse()
            return y == x
            """if y == x:
                return True
            else:
                return False"""
                


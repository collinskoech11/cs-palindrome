"""
Valid Palindrome:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        a_pointer = 0
        b_pointer = len(s) - 1

        while a_pointer < b_pointer:

            while a_pointer < b_pointer and not s[a_pointer].isalnum():
                a_pointer += 1
            while a_pointer < b_pointer and not s[b_pointer].isalnum():
                b_pointer -= 1

            if s[a_pointer].lower() != s[b_pointer].lower():
                return false

            a_pointer += 1
            b_pointer -= 1

        return true


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join([char.lower() for char in s if char.isalnum()])
        i = 0
        while i <= len(s2)/2 - 1:
            j = len(s2) - i - 1
            if s2[i] != s2[j]:
                return False
            i+=1
        return True
             
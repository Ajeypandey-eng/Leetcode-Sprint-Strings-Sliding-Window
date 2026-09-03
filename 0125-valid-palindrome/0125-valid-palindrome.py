class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(clean_s)-1
        while left<right:
            if clean_s[left]==clean_s[right]:
                left+=1
                right-=1
            else:
                return False
        return True       
            
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_len = 0
        max_freq = 0
        counts = {}
        
        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])
            
            # If the number of replacements needed exceeds k, shrink from the left
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
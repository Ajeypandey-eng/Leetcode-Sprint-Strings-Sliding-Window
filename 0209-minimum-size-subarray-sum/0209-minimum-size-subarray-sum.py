class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        min_len=float('inf')
        left=0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum>=target:
                    current_len = right-left+1
                    current_sum -= nums[left]
                    left+=1
                    min_len = min(min_len,current_len)
        return min_len if min_len != float('inf') else 0
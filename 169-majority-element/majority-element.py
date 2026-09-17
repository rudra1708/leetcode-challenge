class Solution(object):
    def majorityElement(self, nums):
        mp={}
        for x in nums:
            mp[x]=mp.get(x,0)+1
        for x in mp:
            if mp[x] >len(nums) // 2:
                return x
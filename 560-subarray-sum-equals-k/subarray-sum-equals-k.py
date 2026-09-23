class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        mp = {0: 1}
        for i in range(len(nums)):
            sums += nums[i]
            count += mp.get(sums - k, 0)
            mp[sums] = mp.get(sums, 0) + 1
        return count
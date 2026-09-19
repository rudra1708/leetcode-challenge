class Solution(object):
    def containsDuplicate(self, nums):
        mp={}
        for ch in nums:
            mp[ch]=mp.get(ch,0)+1
            if mp[ch]>1:
                return True
        return False
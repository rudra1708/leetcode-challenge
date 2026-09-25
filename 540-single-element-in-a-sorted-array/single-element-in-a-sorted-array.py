class Solution(object):
    def singleNonDuplicate(self, nums):
        xor1=0
        for nums in nums:
            xor1=xor1 ^ nums
        return xor1


            




        
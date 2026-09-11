class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2 * n):
            index = i % n
            while stack and nums[index] > nums[stack[-1]]:
                x = stack.pop()
                ans[x] = nums[index]
            if i < n:
                stack.append(index)
        return ans
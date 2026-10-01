class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return []
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        ans = []
        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for num in mp:
                if mp[num] == 0:
                    continue
                mp[num] -= 1
                path.append(num)
                backtrack(path)
                path.pop()
                mp[num] += 1
        backtrack([])
        return ans
class Solution(object):
    def permute(self, nums):
        if not nums:
            return []
        ans = []
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
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
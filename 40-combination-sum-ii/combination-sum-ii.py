class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        n = len(candidates)
        for i in range(n):
            for j in range(0, n - i - 1):
                if candidates[j] > candidates[j + 1]:
                    candidates[j], candidates[j + 1] = candidates[j + 1], candidates[j]
        def backtrack(start, path, curr):
            if curr == target:
                ans.append(path[:])
                return
            if curr > target:
                return
            u = set()
            for i in range(start, n):
                if candidates[i] in u:
                    continue
                u.add(candidates[i])
                path.append(candidates[i])
                backtrack(i + 1, path, curr + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return ans
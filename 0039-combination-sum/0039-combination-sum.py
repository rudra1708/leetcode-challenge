class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        def backtrack(start,path,curr):
            if curr == target:
                result.append(path[:])
                return
            if curr > target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i, path,curr+candidates[i])
                path.pop()
        backtrack(0, [] , 0)
        return result
                
        
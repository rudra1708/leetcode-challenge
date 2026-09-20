class Solution(object):
    def totalFruit(self, fruits):
        left=0
        result=0
        mp={}
        for right in range(len(fruits)):
            ch=fruits[right]
            mp[ch]=mp.get(ch,0)+1
            while len(mp)>2:
                mp[fruits[left]]-=1
                if mp[fruits[left]]==0:
                    del mp[fruits[left]]
                left+=1
            result=max(result,right-left+1)
        return result



        
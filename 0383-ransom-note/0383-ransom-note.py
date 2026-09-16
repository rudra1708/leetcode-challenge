class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mp = {}
        for ch in magazine:
            mp[ch] = mp.get(ch, 0) + 1
        for ch in ransomNote:
            if ch not in mp:
                return False
            if mp[ch] == 0:
                return False
            mp[ch] -= 1
        return True
        
        
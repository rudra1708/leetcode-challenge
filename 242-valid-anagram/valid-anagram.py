class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1

        for ch in t:
            if ch not in mp:
                return False

            mp[ch] -= 1

        for value in mp.values():
            if value != 0:
                return False

        return True
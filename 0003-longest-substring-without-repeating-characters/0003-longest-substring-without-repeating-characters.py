class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        ans = 0
        mp = {}

        for right in range(len(s)):

            ch = s[right]
            mp[ch] = mp.get(ch, 0) + 1

            while mp[ch] > 1:
                mp[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
        
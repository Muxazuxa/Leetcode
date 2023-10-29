class Solution:
    def lengthOfLongestSubstring(self, s):
        result = []
        for i in range(len(s)):
            t = s[i]
            for j in range(i + 1, len(s)):
                if s[j] in t:
                    result.append(t)
                    break
                else:
                    t += s[j]
            result.append(t)
        return len(max(result, key=len))

print(Solution().lengthOfLongestSubstring('pwwkew'))

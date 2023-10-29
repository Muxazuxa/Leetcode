class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            t = s[i]
            for j in range(i + 1, len(s)):
                t += s[j]
                if t == t[::-1]:
                    result.append(t)
        return max(result, key=len) if result else ''


print(Solution().longestPalindrome('cbbd'))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len: int = 0

        substring_len: int = 0
        substring_set: set = set()

        for i in range(len(s)):
            if s[i] not in substring_set:
                substring_len = substring_len + 1
                substring_set.add(s[i])
            else:
                substring_set = set(s[s[:i].rfind(s[i]) + 1:i])
                substring_set.add(s[i])
                substring_len = len(substring_set)

            if substring_len > max_len:
                max_len = substring_len

        return max_len

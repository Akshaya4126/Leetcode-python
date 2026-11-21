class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        count = 0

        for i in s:
            if i in seen:
                seen = seen[seen.index(i) + 1:]

            seen += i
            count = max(count, len(seen))

        return count
        
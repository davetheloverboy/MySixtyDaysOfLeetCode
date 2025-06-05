#Problem: Given a string s, find the length of the longest substring without duplicate characters.
"""
 Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


#use this if in non leetcode format
"""
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",  # 3
        "bbbbb",     # 1
        "pwwkew",    # 3
        "",          # 0
        "au",        # 2
        "dvdf"       # 3
    ]

    for s in test_cases:
        print(f"Input: {s}")
        print(f"Output: {lengthOfLongestSubstring(s)}\n")
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len

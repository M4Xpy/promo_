class Solution(object):
    def lengthOfLongestSubstring(self, string: str) -> int:
        """
        :type string: str
        :rtype: int
        """
        start_index = longest = 0
        diary = {}

        for curr_index, letter in enumerate(string, 1):
            if letter in diary and start_index < diary[letter]:
                start_index = diary[letter]
            else:
                longest = max(longest, curr_index - start_index)
            diary[letter] = curr_index

        return longest

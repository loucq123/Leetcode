class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        current_length = 0
        has_new_last = False
        for c in range(len(s)):
            if s[c] != ' ':
                if has_new_last:
                    current_length = 1
                    has_new_last = False
                else:
                    current_length += 1
            else:
                has_new_last = True
        return current_length
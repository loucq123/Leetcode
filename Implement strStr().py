class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length, haystack_length = len(needle), len(haystack)
        if haystack_length < needle_length:
            return -1
        
        for s in range(haystack_length - needle_length + 1):
            if haystack[s: s + needle_length] == needle:
                return s
        return -1
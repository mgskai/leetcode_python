__author__ = 'mgska'


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        title_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        title_map = {c: (i + 1) for i, c in enumerate(title_string)}
        l = len(s)
        sum = 0
        for c in s:
            l = l - 1
            sum += pow(26, l) * title_map[c]
        return sum

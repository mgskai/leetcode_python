__author__ = 'mgska'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        a = {}
        for n in nums:
            if n in a:
                a[n] += 1
            else:
                a.update({n: 1})
        return max(a, key=lambda x: a[x])

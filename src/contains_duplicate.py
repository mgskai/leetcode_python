__author__ = 'mgska'


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return True if len(set(nums)) != len(nums) else False
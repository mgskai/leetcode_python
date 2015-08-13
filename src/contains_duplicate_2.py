__author__ = 'mgska'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        int_map = set()
        for i, n in enumerate(nums):
            if n in int_map:
                return True
            elif i >= k:
                int_map.remove(nums[i - k])
            int_map.add(nums[i])
        return False

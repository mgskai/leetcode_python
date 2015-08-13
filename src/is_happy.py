__author__ = 'mgska'


class Solution:
    def __pow_sum(self, n):
        return sum(map(lambda x: pow(int(x), 2), str(n)))

    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        int_list = set()
        x = self.__pow_sum(n)
        while 1 not in int_list and x not in int_list:
            int_list.add(x)
            x = self.__pow_sum(x)

        return True if 1 in int_list else False

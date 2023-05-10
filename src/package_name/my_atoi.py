class Solution(object):
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """
        res = positive = ''

        for sign in string.lstrip():
            if sign in '+-':
                positive = sign
                continue
            if sign in '1234567890':
                res += sign
            else:
                break
        if res:
            res = int(positive + res)
            if res > 2147483648:
                return 2147483648
            elif res < -2147483648:
                return -2147483648
            return res
        return 0

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = int(int(str(x)[::-1][:-1])*(-1))
        else:
            result = int(str(x)[::-1])
        if result > (2**31)-1 or result < -2**31:
            result = 0
        return result
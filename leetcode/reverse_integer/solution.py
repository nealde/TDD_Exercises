class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return int(int(str(x)[::-1][:-1])*(-1))
        else:
            return int(str(x)[::-1])
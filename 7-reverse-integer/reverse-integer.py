class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = x < 0
        x = abs(x)
        while x != 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        if negative:
            reverse = -reverse
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0
        return reverse
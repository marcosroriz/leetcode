class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)
        signal = 1
        if (num_str[0] == "-"):
            signal = -1
            num_str = num_str[1:]
        elif (num_str[0] == "+"):
            num_str = num_str[1:]
        
        rev_num_str = num_str[::-1]
        num = signal * int(rev_num_str)

        if (num > (2 ** 31) - 1) or (num < -1 * (2 ** 31)):
            num = 0
        return num


if __name__ == "__main__":
    s = Solution()
    print(321, s.reverse(123))
    print(-321, s.reverse(-123))
    print(32, s.reverse(+32))
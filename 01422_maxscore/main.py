class Solution:
    def maxScore(self, s: str) -> int:
        newstr: list = []

        curr_substring = None
        sumof0 = 0
        sumof1 = 0

        # first case
        newstr.append(1 if int(s[0]) == 1 else -1)

        # remainder cases
        for i in range(1, len(s) - 1):
            curr_num: int = int(s[i])
            if curr_num == 0 and (curr_substring == 0 or curr_substring is None):
                sumof0 = sumof0 - 1
            elif curr_num == 0 and curr_substring == 1:
                newstr.append(sumof1)
                sumof1 = 0
                sumof0 = -1
            elif curr_num == 1 and curr_substring == 0:
                newstr.append(sumof0)
                sumof1 = 1
                sumof0 = 0
            elif curr_num == 1 and (curr_substring == 1 or curr_substring is None):
                sumof1 = sumof1 + 1

            curr_substring = curr_num

        if curr_substring == 0:
            newstr.append(sumof0)
        elif curr_substring == 1:
            newstr.append(sumof1)

        # Last element
        newstr.append(1 if int(s[-1]) == 1 else -1)

        max_sum = 0
        interval = range(1, len(newstr)) if len(s) > 2 else range(1, len(newstr))
        for i in interval:
            left_part = newstr[:i]
            right_part = newstr[i:]

            sum_left_0s = -1 * sum(filter(lambda e: e < 0, left_part))
            sum_right_1s = sum(filter(lambda e: e > 0, right_part))
            elem_sum = sum_left_0s + sum_right_1s
            if elem_sum > max_sum:
                max_sum = elem_sum

        return max_sum


if __name__ == "__main__":
    s = Solution()
    print("01001", s.maxScore("01001"))
    print("00", s.maxScore("00"))
    print("11", s.maxScore("11"))
    print("11101", s.maxScore("11101"))
    print("00111", s.maxScore("00111"))
    print("1111", s.maxScore("1111"))

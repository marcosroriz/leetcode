class Solution:
    def parseSubstr(self, substr: str) -> int:
        # Basic case
        if substr.isnumeric():
            return int(substr)

        # Valid cades for empty and size one substrings
        if len(substr) == 0 or (len(substr) == 1 and (substr[0] == "+" or substr[0] == "-")):
            return 0

        # More complex cases, lets check if has special char (+, -, .)
        # While doing so, we add valid numbers to numlist, which we will then transform to num back
        numlist = []
        for i in range(len(substr)):
            if i == 0 and (substr[i] == "+" or substr[i] == "-"):
                numlist.append(substr[i])
                continue
            elif i != 0 and (substr[i] == "." or not substr[i].isdigit()):
                break
            
            numlist.append(substr[i])
        
        num = "".join(numlist)
        
        if len(num) == 0:
            return 0
        elif len(num) == 1 and (num[0] == "+" or num[0] == "-"):
            return 0
        elif num.isnumeric() or ((num[0] == "+" or num[0] == "-") and num[1:].isnumeric()):
            return int(num)
        else:
            return 0

    def myAtoi(self, s: str) -> int:
        num = 0
        substr = ""
        for ss in s.split(" "):
            if len(ss) == 0:
                continue

            substr = ss
            break

        num = self.parseSubstr(substr)
        num = min(num, 2 ** 31 - 1)
        num = max(-(2 ** 31), num)

        return num


if __name__ == "__main__":
    s = Solution()
    print("+-12", s.myAtoi("+-12"))
    print("0012a42", s.myAtoi("  -0012a42"))
    print(3.14159, s.myAtoi("3.14159"))
    print(-42, s.myAtoi("   -42"))
    print(987, s.myAtoi("words and 987"))

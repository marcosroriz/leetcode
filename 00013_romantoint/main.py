class Solution:
    def parseI(self, next_char="") -> (int, bool):
        peaked = False
        val = 1
        if next_char == "V":
            peaked = True
            val = 4
        elif next_char == "X":
            peaked = True
            val = 9

        return (val, peaked)

    def parseV(self, next_char="") -> (int, bool):
        return (5, False)

    def parseX(self, next_char="") -> (int, bool):
        peaked = False
        val = 10
        if next_char == "L":
            peaked = True
            val = 40
        elif next_char == "C":
            peaked = True
            val = 90

        return (val, peaked)

    def parseL(self, next_char="") -> (int, bool):
        return (50, False)

    def parseC(self, next_char="") -> (int, bool):
        peaked = False
        val = 100
        if next_char == "D":
            peaked = True
            val = 400
        elif next_char == "M":
            peaked = True
            val = 900

        return (val, peaked)

    def parseD(self, next_char="") -> (int, bool):
        return (500, False)

    def parseM(self, next_char="") -> (int, bool):
        return (1000, False)

    def romanToInt(self, s: str) -> int:
        num = 0
        str_size = len(s)
        max_index = str_size - 1
        i = 0
        while i < str_size:
            next_char: str = s[i + 1] if i + 1 <= max_index else ""
            parse_func = None
            
            if s[i] == "I":
                parse_func = self.parseI
            elif s[i] == "V":
                parse_func = self.parseV
            elif s[i] == "X":
                parse_func = self.parseX
            elif s[i] == "L":
                parse_func = self.parseL
            elif s[i] == "C":
                parse_func = self.parseC
            elif s[i] == "D":
                parse_func = self.parseD
            elif s[i] == "M":
                parse_func = self.parseM

            val, peaked = parse_func(next_char)
            num = num + val
            
            if peaked:
                i = i + 2
            else:
                i = i + 1

        return num


if __name__ == "__main__":
    s = Solution()
    print("III", 3, s.romanToInt("III"))
    print("IV", 4, s.romanToInt("IV"))
    print("IX", 9, s.romanToInt("IX"))
    print("LVIII", 58, s.romanToInt("LVIII"))
    print("MCMXCIV", 1994, s.romanToInt("MCMXCIV"))

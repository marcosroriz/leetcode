from typing import List


class Solution:
    def isValidLine(self, line: List[str]) -> bool:
        valid = True
        nums = set()

        for n in filter(lambda m: m != ".", line):
            if n in nums:
                valid = False
                break
            else:
                nums.add(n)

        return valid

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True

        # Lines
        for i in range(9):
            v = self.isValidLine(board[i])
            if not v:
                valid = False
                break

        # Columns
        for j in range(9):
            line = [board[i][j] for i in range(9)]
            v = self.isValidLine(line)
            if not v:
                valid = False
                break

        # 3x3
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                line = [board[a][b] for a in range(i, i + 3) for b in range(j, j + 3)]
                v = self.isValidLine(line)
                if not v:
                    valid = False
                    break
                j = j + 3

            if not valid:
                break
            i = i + 3

        return valid


if __name__ == "__main__":
    s = Solution()
    print(
        True,
        s.isValidSudoku(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
    )

    print(
        False,
        s.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        ),
    )

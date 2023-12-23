from typing import List 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(lambda d: str(d), digits))) + 1
        return list(map(lambda d: int(d), str(num)))

if __name__ == "__main__":
    s = Solution()
    print([1,2,3], s.plusOne([1,2,3]))
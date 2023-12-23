class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        points.add((0, 0))
        crossed = False

        x = 0
        y = 0
        
        for move in path:
            if (move == "N"):
                y = y + 1
            elif (move == "S"):
                y = y - 1
            elif (move == "E"):
                x = x + 1
            elif (move == "W"):
                x = x - 1
            
            if ((x, y) in points):
                crossed = True
                break
            else:
                points.add((x, y))
            
        return crossed

if __name__ == "__main__":
    s = Solution()
    print("NES", s.isPathCrossing("NES"))
    print("NESWW", s.isPathCrossing("NESWW"))
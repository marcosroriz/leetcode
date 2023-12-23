from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # add extra padding to enable right size peek
        height.append(0)

        map_size = len(height)
        peak_height = 0
        left_peak = 0
        max_right_peak = 0
        right_peak = 0
        left_peak_reached = False
        right_peak_reached = False

        map_index = 0
        left_index = 0
        right_index = 0
        max_right_index = 0

        total_water = 0


        while left_index < right_index + 1:         
            while not left_peak_reached and left_index < map_size - 1:
                curr_height = height[left_index]
                next_height = height[left_index + 1]
                if curr_height > next_height:
                    left_peak = curr_height
                    left_peak_reached = True
                    break
                else:
                    left_index = left_index + 1

            right_index = left_index + 1
            while right_index < map_size - 1:
                prev_height = height[right_index - 1]
                curr_height = height[right_index]
                next_height = height[right_index + 1]
                
                if curr_height >= prev_height and curr_height > next_height:
                    right_peak_reached = True
                    right_peak = curr_height

                    if right_peak > max_right_peak:
                        max_right_peak = right_peak
                        max_right_index = right_index

                    if right_peak >= left_peak:
                        break
                right_index = right_index + 1

            peak_height = min(left_peak, max_right_peak)
            while left_index < max_right_index and right_peak_reached:
                curr_height = height[left_index]
                total_water = total_water + max(0, (peak_height - curr_height))
                left_index = left_index + 1

            if not right_peak_reached:
                break
            
            map_index = max_right_index
            left_index = max_right_index
            left_peak = max_right_peak
            max_right_peak = 0
            left_peak_reached = True
            right_peak_reached = False

        return total_water


if __name__ == "__main__":
    s = Solution()
    print(3, s.trap([9,6,8,8,5,6,3]))
    print(9, s.trap([4,2,0,3,2,5]))
    print(5, s.trap([0,5,5,0,0,0,0,5]))
    print(6, s.trap([0, 6, 0, 0, 6, 0, 0]))
    print(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3]))
    print(8, s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

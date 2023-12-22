from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        size = len(nums)
        i_ans = None
        j_ans = None
        i_elem = None
        j_elem = None
        found = False
        for i in range(size - 1):
            # Before trying, lets see if sum to biggest is smaller than target, if true, jump to next candidate
            if nums_sorted[i] + nums_sorted[size - 1] < target:
                continue

            # OK, lets try this guy with the remainder j's
            j = i + 1
            while (j < size):
                # Check if we can do a big jump in j
                if nums_sorted[i] + nums_sorted[(j + size) // 2] < target:
                    j = (j + size) // 2
                    continue

                # Check if we hit the target
                if nums_sorted[i] + nums_sorted[j] == target:
                    i_elem = nums_sorted[i]
                    j_elem = nums_sorted[j]
                    found = True

                # If fail, see if our sum is bigger, if true breaks
                if nums_sorted[i] + nums_sorted[j] > target:
                    break

                j = j + 1

            if found:
                break

        if i_elem != j_elem:
            i_ans = next(i for i in range(size) if nums[i] == i_elem)
            j_ans = next(j for j in range(size) if nums[j] == j_elem)
        else:
            i_ans = next(i for i in range(size) if nums[i] == i_elem)
            j_ans = next(j for j in range(
                i_ans + 1, size) if nums[j] == j_elem)

        return (i_ans, j_ans)

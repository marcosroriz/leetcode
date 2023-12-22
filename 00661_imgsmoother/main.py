from math import floor
from typing import List


class Solution:
    def point_smooth(self, img: List[List[int]]) -> List[List[int]]:
        return [[floor(img[0][0])]]

    def line_smooth(self, img: List[List[int]], num_rows, num_columns) -> List[List[int]]:
        result = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

        for j in range(num_columns):
            elem = 0
            div = 3
            
            if j != 0 and j != num_columns - 1:
                elem = img[0][j - 1] + img[0][j] + img[0][j + 1]
            elif j == 0:
                elem = img[0][j] + img[0][j + 1]
                div = 2
            elif j == num_columns - 1:
                elem = img[0][j - 1] + img[0][j]
                div = 2

            result[0][j] = floor(elem / div)

        return result

    def column_smooth(self, img: List[List[int]], num_rows, num_columns) -> List[List[int]]:
        result = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

        for i in range(num_rows):
            elem = 0
            div = 3
            if i != 0 and i != num_rows - 1:
                elem = img[i - 1][0] + img[i][0] + img[i + 1][0]
            elif i == 0:
                elem = img[i][0] + img[i + 1][0]
                div = 2
            elif i == num_rows - 1:
                elem = img[i - 1][0] + img[i][0]
                div = 2

            result[i][0] = floor(elem / div)

        return result

    def matrix_smooth(self, img: List[List[int]], num_rows, num_columns) -> List[List[int]]:
        pad_img = [[0 for _ in range(num_columns + 2)]
                   for _ in range(num_rows + 2)]
        result = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_columns):
                pad_img[i+1][j+1] = img[i][j]

        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                line_top = sum(pad_img[i - 1][j - 1:j + 2])
                line_median = sum(pad_img[i][j - 1:j + 2])
                line_bottom = sum(pad_img[i+1][j - 1:j + 2])
                elem = line_top + line_median + line_bottom

                div = 9
                if ((i == 1 and j == 1) or (i == 1 and j == num_columns) or
                        (i == num_rows and j == 1) or (i == num_rows and j == num_columns)):
                    div = 4
                elif (i == 1) or (i == num_rows) or (j == 1) or (j == num_columns):
                    div = 6

                result[i-1][j-1] = floor(elem / div)

        return result

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        num_rows = len(img)
        num_columns = len(img[0])

        if num_rows > 1 and num_columns > 1:
            return self.matrix_smooth(img, num_rows, num_columns)
        elif num_rows == 1 and num_columns == 1:
            return self.point_smooth(img)
        elif num_rows == 1 and num_columns != 1:
            return self.line_smooth(img, num_rows, num_columns)
        elif num_rows != 1 and num_columns == 1:
            return self.column_smooth(img, num_rows, num_columns)

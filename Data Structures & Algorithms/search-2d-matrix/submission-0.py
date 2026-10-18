class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])*len(matrix)-1

        while l<=r:
            mid = (r + l)//2
            mrow = mid // len(matrix[0])
            mcol = mid % len(matrix[0])

            if matrix[mrow][mcol] > target:
                r = mid - 1
            elif matrix[mrow][mcol] < target:
                l = mid + 1
            else:
                return True
        return False

        
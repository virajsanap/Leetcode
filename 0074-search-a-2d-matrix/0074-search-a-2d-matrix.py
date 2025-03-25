class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot =0,rows-1

        while(top<=bot):
            mid = (top+bot)//2
            if matrix[mid][0]<target and matrix[mid][-1]> target:
                break
            elif matrix[mid][0]>target:
                bot=mid-1
            else:
                top=mid+1
        row=(top+bot)//2        
        l=0
        r=cols-1
        while(l<=r):
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l=m+1
            else:
                r=m-1
        return False
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        result=[1,1]
        for i in range(1,rowIndex):
            newRow=[1]
            for j in range(len(result)-1):
                newRow.append(result[j]+result[j+1])
            newRow.append(1)
            result=newRow
        return result
    
        
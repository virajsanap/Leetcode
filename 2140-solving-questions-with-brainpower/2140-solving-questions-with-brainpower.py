class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*len(questions)
        for i in range(len(questions)-1,-1,-1):
            index=i+questions[i][1]+1
            print(i,index)
            if index < len(questions):
                dp[i] = dp[index]+questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i<len(questions)-1:
                dp[i]=max(dp[i+1],dp[i])
        return dp[0]
        
        
        
        
        # mostpoints=0
        # for i in range(len(questions)):
        #     points=0
        #     j=i
        #     while j<len(questions):
        #         points+=questions[j][0]
        #         j+=questions[j][1]+1
        #     mostpoints = max(mostpoints,points)
        #     print(f"{i}=>{mostpoints}")
        
        # return mostpoints
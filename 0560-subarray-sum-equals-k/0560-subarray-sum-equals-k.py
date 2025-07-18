class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num={0:1}
        temp_sum=0
        count=0
        for num in nums:
            temp_sum+=num
            if temp_sum-k in sub_num:
                count+=sub_num[temp_sum-k]
            sub_num[temp_sum] = 1+sub_num.get(temp_sum,0)
        return count
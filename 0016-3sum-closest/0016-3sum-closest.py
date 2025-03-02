class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        closest_sum = float('inf')
        for i in range(n-2):
            print(f"i:{i}")
            l,r=i+1,n-1
            print(f"l:{l},r:{r}")
            print(f"left:{nums[l]}, right:{nums[r]}")
            while(l<r):
                current_sum = nums[i]+nums[l]+nums[r]
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                if current_sum<target:
                    l+=1
                elif current_sum>target:
                    r-=1
                else:
                    return current_sum
        return closest_sum

        

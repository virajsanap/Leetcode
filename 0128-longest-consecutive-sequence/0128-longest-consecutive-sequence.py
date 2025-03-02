class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        num_set = set(nums)
        print(num_set)
        longest=0
        current_streak = 0
        for i in num_set:
            if i-1 not in  num_set:
                current_streak=1
                while i+current_streak in num_set:
                    current_streak+=1
                longest=max(longest, current_streak)
        return longest
        
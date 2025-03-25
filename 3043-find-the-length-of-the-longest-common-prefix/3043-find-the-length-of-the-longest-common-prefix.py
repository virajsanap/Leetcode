class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = {}
        for num in arr1:
            str_num=str(num)
            prefix=""
            for ch in str_num:
                prefix+=ch
                prefix_map[prefix] = prefix_map.get(prefix,0)+1
        print(prefix_map)
        max_len =0 
        for num in arr2:
            str_num = str(num)
            prefix=""
            for ch in str_num:
                prefix+=ch
                print(prefix)
                if prefix in prefix_map:
                    max_len = max(max_len,len(prefix))
        
        return max_len
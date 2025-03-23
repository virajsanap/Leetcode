class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums= { 
                '1': [],
                '2': ["a","b","c"],
                '3': ["d","e","f"],
                '4': ["g","h","i"],
                '5': ["j","k","l"],
                '6': ["m","n","o"],
                '7': ["p","q","r","s"],
                '8': ["t","u","v"],
                '9': ["w","x","y","z"],
                '0': []
            }
        res=[]
        if not digits:
            return []
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return 
            for letter in nums[next_digits[0]]:
                backtrack(combination+letter, next_digits[1:])
        
        backtrack("", digits)
        
        return res    
        
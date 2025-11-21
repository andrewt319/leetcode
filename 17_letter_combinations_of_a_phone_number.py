class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def bt(idx, curr):
            if idx >= len(digits):
                sol.append(curr)
                return
  
            for c in mapping[digits[idx]]:
                bt(idx + 1, curr + c)
            return 

        bt(0, '')
        return sol

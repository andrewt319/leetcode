class Solution:
    def isHappy(self, n: int) -> bool:
        def getSquareOfDigits(n):
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            return total
        
        slow = fast = n
        while True:
            slow = getSquareOfDigits(slow)
            fast = getSquareOfDigits(getSquareOfDigits(fast))

            if slow == 1 or fast == 1:
                return True
            elif slow == fast:
                return False

        # O(N) space
        # visited = set()
        # visited.add(n)

        # while n != 1:
        #     curr = 0
        #     for c in str(n):
        #         curr += int(c)**2
        #     if curr in visited:
        #         return False
        #     visited.add(curr)
        #     n = curr

        # return True


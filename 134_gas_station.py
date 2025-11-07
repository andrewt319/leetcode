class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currTank = totalTank = idx = 0

        for i in range(len(gas)):
            # You need total gas to be > total cost in order for it to be possible to travel
            # around, so should track this
            totalTank += gas[i] - cost[i]

            # Optimistically assume the next point after your tank is empty could be your start index.
            # If gas[i] - cost[i] is positive at idx 1, 2 and 3, you start at the first one. 
            currTank += gas[i] - cost[i]
            if currTank < 0:
                currTank = 0
                idx = (i + 1) % len(gas)
        
        return idx if totalTank >= 0 else -1

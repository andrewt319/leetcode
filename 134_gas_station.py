class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = totalCost = currGas = idx = 0

        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]

            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                idx = i + 1
        
        return idx if totalGas >= totalCost else -1


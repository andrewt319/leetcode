class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = []
        timeToTarget = []
        numFleets = 1

        for i in range(len(position)):
            posAndSpeed.append((position[i], speed[i]))
        
        posAndSpeed.sort()
        for i in range(len(posAndSpeed)):
            timeToTarget.append((target - posAndSpeed[i][0]) / posAndSpeed[i][1])

        slowest = timeToTarget[-1]
        for i in range(len(timeToTarget) - 2, -1, -1):
            if timeToTarget[i] > slowest:
                numFleets += 1
                slowest = timeToTarget[i]

        return numFleets

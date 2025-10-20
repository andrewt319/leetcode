class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        sol = float('-inf')

        print(heaters)
        for house in houses:
            idx = bisect.bisect_right(heaters, house)

            leftHeaterPos = heaters[idx - 1] if idx > 0 else heaters[0]
            rightHeaterPos = heaters[idx] if idx < len(heaters) else heaters[-1]

            closest = min(abs(house - leftHeaterPos), abs(rightHeaterPos - house))
            sol = max(sol, closest)
        
        return sol

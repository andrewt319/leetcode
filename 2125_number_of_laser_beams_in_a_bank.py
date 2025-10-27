class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sol = prevNumSecurityDevices = 0

        for plan in bank:
            currNumSecurityDevices = plan.count('1')
            
            if currNumSecurityDevices != 0:
                sol += currNumSecurityDevices * prevNumSecurityDevices
                prevNumSecurityDevices = currNumSecurityDevices

        return sol

            


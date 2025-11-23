from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n, m = len(votes), len(votes[0])
        teamToVotesMap = defaultdict(lambda: [0] * m)

        for i in range(n):
            for j, team in enumerate(votes[i]):
                teamToVotesMap[team][j] -= 1
        
        sortedList = sorted(teamToVotesMap.items(), key=lambda x: (x[1], x[0]))
        return ''.join(item[0] for item in sortedList)


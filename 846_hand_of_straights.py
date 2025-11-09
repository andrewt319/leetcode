
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        hand.sort()
        for i in range(len(hand)):
            if (i > 0 and hand[i] == hand[i - 1]) or (counts[hand[i]] == 0):
                continue

            goalCount = counts[hand[i]]
            for nxt in range(hand[i] + 1, hand[i] + groupSize):
                counts[nxt] -= goalCount
                if counts[nxt] < 0:
                    return False
        
        return True
                

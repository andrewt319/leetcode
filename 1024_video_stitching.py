class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        if clips[0][0] != 0:
            return -1
        
        numClips = 1
        prevStart, prevEnd = clips[0]
        for i in range(1, len(clips)):
            currStart, currEnd = clips[i]

            if prevEnd >= time:
                return numClips
            elif currStart > prevEnd:
                return -1
            elif currEnd > prevEnd and currStart > prevStart:
                numClips += 1
                prevStart = max(prevEnd, currStart)
                prevEnd = currEnd
            elif currEnd > prevEnd and currStart <= prevStart:
                prevEnd = currEnd
        
        return numClips if prevEnd >= time else -1
        

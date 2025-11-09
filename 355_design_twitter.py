from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.userToPosts = defaultdict(list)
        self.userToFollowing = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToPosts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        newsFeed = []
        candidates.extend(self.userToPosts[userId][-10:])
        for user in self.userToFollowing[userId]:
            candidates.extend(self.userToPosts[user][-10:])
        heapq.heapify(candidates)

        while len(newsFeed) < 10 and candidates:
            _, tweetId = heapq.heappop(candidates)
            newsFeed.append(tweetId)
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollowing[followerId]:
            self.userToFollowing[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Tweet:
    '''
    single tweet class
    we just need the tweet id and the time of creation
    '''
    def __init__(self,tID,time):
        self.tID = tID
        self.time = time
        
class Twitter(object):
    '''
    the solution is that we need 2 hashmaps (tables) here
    one - for the all the users a user is following, like uID1:[uID2,uID3,uID5,UID1,...]
    for a user the particular user himself becomes a follower since it would be 
    easy to retrieve the users individual tweets also
    two - a tweets hashMap like uID1:[tID1,tID2,tID3,...]
    where tIDs are individual tweets of the users followers and the user itself
    
    we will also use a priority queue min heap with a size of 10 as mentioned in the problem
    so the time with min time meaning the one earliest created will be at the top
    and will be removed when queue overflows
    '''
    def __init__(self):
        self.time = 0
        self.followers = {}
        self.tweets = {}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        '''
        create tweet with global time and tweetId
        '''
        self.follow(userId, userId) #adding the user himself to list of people he is following
        
        if userId not in self.tweets:
            self.tweets[userId] = []
            
        tweet = Tweet(tweetId,self.time)
        self.time+=1
        
        self.tweets.get(userId).append(tweet)
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        Tweet.__lt__ = (lambda a, b:  a.time  < b.time)
        result = []
        posts = []
        
        followers = self.followers.get(userId)
        
        if followers:
            for f in followers:
                tweets = self.tweets.get(f)
                if tweets:
                    for t in tweets:
                        heappush(posts, t)
                        if len(posts) > 10:
                            heappop(posts)
        while posts:
            result.append(heappop(posts).tID)
        
        return result[::-1]
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        '''
        twitter.follow(1, 2);    // User 1 follows user 2.
        we add user 2 to user 1's list of followers
        '''
        if not followerId in self.followers:
            self.followers[followerId] = set([followeeId]) 
            #using a set since we dont want same followeeId's to be repeated
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        '''
        twitter.unfollow(1, 2);  // User 1 unfollows user 2.
        '''
        if followerId in self.followers and followerId != followeeId:
            self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
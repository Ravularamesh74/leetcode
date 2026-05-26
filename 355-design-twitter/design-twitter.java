import java.util.*;

class Twitter {

    private static class Tweet {
        int id;
        int time;
        Tweet next;

        Tweet(int id, int time) {
            this.id = id;
            this.time = time;
        }
    }

    private int timestamp;

    private Map<Integer, Set<Integer>> followMap;
    private Map<Integer, Tweet> tweetMap;

    public Twitter() {
        timestamp = 0;
        followMap = new HashMap<>();
        tweetMap = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {

        Tweet tweet = new Tweet(tweetId, timestamp++);

        tweet.next = tweetMap.get(userId);

        tweetMap.put(userId, tweet);
    }

    public List<Integer> getNewsFeed(int userId) {

        List<Integer> result = new ArrayList<>();

        PriorityQueue<Tweet> pq =
                new PriorityQueue<>(
                        (a, b) -> b.time - a.time
                );

        if (tweetMap.containsKey(userId)) {
            pq.offer(tweetMap.get(userId));
        }

        Set<Integer> follows =
                followMap.getOrDefault(
                        userId,
                        new HashSet<>()
                );

        for (int followee : follows) {
            if (tweetMap.containsKey(followee)) {
                pq.offer(tweetMap.get(followee));
            }
        }

        while (!pq.isEmpty() && result.size() < 10) {

            Tweet curr = pq.poll();

            result.add(curr.id);

            if (curr.next != null) {
                pq.offer(curr.next);
            }
        }

        return result;
    }

    public void follow(int followerId, int followeeId) {

        followMap
                .computeIfAbsent(
                        followerId,
                        k -> new HashSet<>()
                )
                .add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {

        if (followMap.containsKey(followerId)) {
            followMap.get(followerId)
                     .remove(followeeId);
        }
    }
}
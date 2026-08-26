import heapq

class MedianFinder(object):

    def __init__(self):
        # max-heap stores the smaller half (invert sign for max-heap in Python)
        self.small = []
        # min-heap stores the larger half
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Always push to small heap first
        heapq.heappush(self.small, -num)
        
        # Ensure max element of small <= min element of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes (small heap can have at most 1 extra element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
       
        max_cost = max(costs)

        # Count frequency of each cost
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        ans = 0

        # Buy from cheapest to most expensive
        for cost in range(1, max_cost + 1):
            if freq[cost] == 0:
                continue

            can_buy = min(freq[cost], coins // cost)
            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 1, -1, -1):
            if i < len(cost) - 2:
                one = i + 1
                two = i + 2
                cost[i] = min(cost[one] + cost[i], cost[two] + cost[i])
        return min(cost[0], cost[1])   
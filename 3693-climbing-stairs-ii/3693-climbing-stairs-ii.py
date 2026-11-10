class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        mincost=[float('inf'), float('inf'), 0] + [0]*len(costs)
        for i  in   range(3,len(mincost)):
            mincost[i]=costs[i-3]+min(mincost[i-3]+9,mincost[i-2]+4,mincost[i-1]+1)
        return mincost[-1]
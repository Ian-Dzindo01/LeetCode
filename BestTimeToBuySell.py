class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    mani, lptr = 0, 0
    for rptr in range(1, len(prices)):
        if prices[lptr] < prices[rptr]:
            mani = max(mani, prices[rptr] - prices[lptr])
        else:
            lptr = rptr

    return mani

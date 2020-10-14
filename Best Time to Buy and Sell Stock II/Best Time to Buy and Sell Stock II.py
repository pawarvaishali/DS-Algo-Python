# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:27:11 2020

@author: VSP021
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                maxprofit += prices[i+1] - prices[i]
                
        print(maxprofit)
        return maxprofit
        
if __name__ == "__main__":
    obj = Solution()
    prices = [7,1,5,3,6,4]
    print(obj.maxProfit(prices))
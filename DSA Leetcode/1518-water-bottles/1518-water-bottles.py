class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + math.floor((numBottles-1) /(numExchange-1)) 
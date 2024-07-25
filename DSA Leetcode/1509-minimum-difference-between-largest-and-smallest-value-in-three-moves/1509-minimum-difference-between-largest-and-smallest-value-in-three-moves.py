class Solution:
    def minDifference(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        if(length<=4):
            return 0
        else:
            diff1=nums[length-4]-nums[0]
            diff2=nums[length-1]-nums[3]
            diff3=nums[length-2]-nums[2]
            diff4=nums[length-3]-nums[1]
            min_diff = min(diff1, diff2, diff3, diff4)
        return min_diff

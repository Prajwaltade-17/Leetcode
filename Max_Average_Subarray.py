class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_window=sum(nums[:k])
        max_avg=max_window/k
        for i in range(k,len(nums)):
            max_window+=nums[i]
            max_window-=nums[i-k]
            max_avg=max(max_avg,max_window/k)
        return max_avg
                

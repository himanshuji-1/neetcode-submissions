class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        target = []

        for i in range(len(nums)-k+1):
          window = nums[i:i+k]
          target.append(max(window))

        return target
# Concluído
# Runtime: 55ms
# Memory: 16.1MB

class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        trigg = 0
        for i in range(len(nums)-1):
          for j in range(i+1,len(nums)):
            if nums[i] + nums[j] < target:
              trigg += 1

        return trigg
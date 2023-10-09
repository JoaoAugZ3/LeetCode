# Concluído
# Runtime: 74ms
# Memory: 16.5MB

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        right = [0]
        answer = []
        x = 0
        for i in range(len(nums)-1):
            sum = left[i] + nums[i]
            left.append(sum)
        
        for i in range(len(nums)-1, 0, -1):
            sum = right[x] + nums[i]
            x += 1
            right.append(sum)
        right.reverse()    
        for i in range(len(nums)):
            sum = left[i] - right[i]
            answer.append(abs(sum))

        return answer
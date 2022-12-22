
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            curr = nums[i]
            j = i+1
            while curr + nums[j] != target and j < len(nums)-1:
                j+=1
            if curr + nums[j] == target:
                break
        return [i, j]

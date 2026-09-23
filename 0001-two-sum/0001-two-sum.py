class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if (target-nums[i])in nums:
                if i!=nums.index(target-nums[i]):
                    return[i,nums.index(target-nums[i])]
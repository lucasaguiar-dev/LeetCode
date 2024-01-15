class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            array.append(count)
        return array


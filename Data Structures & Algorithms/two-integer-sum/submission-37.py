class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_dict = {}

        # go through the nums list and add first num seen to the temp_dict dictionary
        for i, num in enumerate(nums):
            if i == 0:
                temp_dict[num] = i
                continue
            
            diff = target - nums[i]
            if diff in temp_dict and temp_dict[diff] != i:
                if i < temp_dict[diff]:
                    result = [i, temp_dict[diff]]
                if i > temp_dict[diff]:
                    result = [temp_dict[diff], i]
            else:
                temp_dict[num] = i
        return result
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_dict = {}

        for i, num in enumerate(nums):
            if num not in temp_dict:
                temp_dict[num] = i

            diff = target - num
            if diff in temp_dict and temp_dict[diff] != i:
                if i < temp_dict[diff]:
                    result = [i, temp_dict[diff]]
                else:
                    result = [temp_dict[diff], i]
        
        return result
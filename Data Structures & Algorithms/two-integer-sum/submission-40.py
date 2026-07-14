class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_dict = {} # store {number: index} for numbers we've already seen

        # iterate thru the list once
        for i, num in enumerate(nums):
            # for the current number, calculate the number needed to reach the target
            diff = target - num
            # if we've already seen the required number (diff), yay we found the pair, return the two indices
            if diff in temp_dict and temp_dict[diff] != i:
                if i < temp_dict[diff]:
                    result = [i, temp_dict[diff]]
                else:
                    result = [temp_dict[diff], i]
            # if we have not seen the number, just remember this current number by storing in temp_dict dictionary for future iterations
            else:
                temp_dict[num] = i
        return result
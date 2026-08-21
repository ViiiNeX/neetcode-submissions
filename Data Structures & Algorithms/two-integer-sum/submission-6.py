class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_numbers = {}
        
        for index,anumber in enumerate(nums):
            other_pair = target - anumber

            if other_pair not in checked_numbers:

                checked_numbers[anumber] = index
            
            else:
                return [checked_numbers[other_pair],index]

            

                
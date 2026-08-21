class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_numbers = {}
        
        for index,anumber in enumerate(nums):
            other_pair = target - anumber

            
            if other_pair in checked_numbers:

                return [checked_numbers[other_pair],index]
            
            else:
                
                checked_numbers[anumber] = index

            

                
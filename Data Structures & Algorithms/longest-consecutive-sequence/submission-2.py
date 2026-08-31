class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = [2,20,4,10,3,4,5]

        nums_set = set(nums)
        longest = 0


        for n in nums:
            if n-1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                longest = max(length,longest)

        return longest
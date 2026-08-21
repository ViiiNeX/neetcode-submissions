class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        number_checker = []
        for anumber in nums:
            if anumber in number_checker:
                return True

            else:
                number_checker.append(anumber)

        return False

        
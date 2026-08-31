class Solution:

    def check_s(self,c):

        return (ord("a") <= ord(c) <= ord("z")
        or      ord("A") <= ord(c) <= ord("Z")
        or      ord("0") <= ord(c) <= ord("9"))
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for char in s:
            if self.check_s(char):
                clean += char
        
        l = 0
        r = len(clean) - 1

        while l < r:
            if clean.lower()[l] == clean.lower()[r]:
                l += 1
                r -= 1
            else:
                return False



        return True
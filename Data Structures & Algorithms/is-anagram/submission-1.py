class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_1 = sorted(list(s))
        letters_2 = sorted(list(t))

        if letters_1 == letters_2:
            return True

        else:
            return False

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        all_letters = string.ascii_letters 
        digits = string.digits   
        alphanumeric = all_letters + digits
        clean = []
        for char in s:
            if char in alphanumeric:
                clean.append(char)
        clean2 = "".join(clean)
        no_spaces = clean2.replace(" ", "")
        all_lower = no_spaces.lower()


        reversed_str = (list(clean2))[::-1]
        merged_str = "".join(reversed_str)
        no_spaces_rev = merged_str.replace(" ", "")
        
        all_lower_rev = no_spaces_rev.lower()


        if all_lower == all_lower_rev:
            return True
        return False

        
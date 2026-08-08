class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        same_words = {}
        for word in strs:
            sorted_letters = "".join(sorted(list(word)))
            if sorted_letters not in same_words:
                same_words[sorted_letters] = [word,]

            elif sorted_letters in same_words:
                same_words[sorted_letters].append(word)

        for key,value in same_words.items():
            result.append(value)

        return result
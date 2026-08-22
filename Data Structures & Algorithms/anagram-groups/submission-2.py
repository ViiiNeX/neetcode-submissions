class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    #strs = ["act","pots","tops","cat","stop","hat"]
        letter_map = defaultdict(list)

        for astring in strs:
            adjusted_key = str(sorted(astring))

            letter_map[adjusted_key].append(astring)


        result = []
        for values in letter_map.values():
            result.append(values)

        return result
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = defaultdict(list)
        for i in range(len(strs)):
            sorted_key = str(sorted(strs[i]))
            an_map[sorted_key].append(strs[i])
        ans_list = []
        for key in an_map:
            ans_list.append(an_map[key])
        return ans_list

        
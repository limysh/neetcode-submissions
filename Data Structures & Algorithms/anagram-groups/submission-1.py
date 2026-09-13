from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = defaultdict(list)
        for i in range(len(strs)):
            # sorted_key = str(sorted(strs[i]))
            freq = [0] * 26
            for j in range(len(strs[i])):
                key_freq = ord('a') - ord(strs[i][j])
                freq[key_freq] += 1
            sorted_key = tuple(freq)
            an_map[sorted_key].append(strs[i])
        ans_list = []
        for key in an_map:
            ans_list.append(an_map[key])
        return ans_list

        
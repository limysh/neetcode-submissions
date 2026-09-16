from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        i = 0
        j = 1
        freq_map[s[i]] += 1
        max_freq = 1
        max_len = 1
        while j < len(s):
            freq_map[s[j]] += 1  
            max_freq = max(max_freq, freq_map[s[j]])
            if (j - i + 1) - max_freq <= k:
                max_len = max(max_len, j-i+1)
                j += 1
            else:
                freq_map[s[i]] -= 1
                i += 1
                j += 1
            
        return max_len






        
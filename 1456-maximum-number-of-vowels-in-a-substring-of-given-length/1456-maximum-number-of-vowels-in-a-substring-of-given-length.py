class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0

        for i in range(k):
            if (self.vowel_check(s[i])):
                count += 1
        
        max_count = count
        for i in range(k, len(s)):
            if (self.vowel_check(s[i])):
                count += 1
            if (self.vowel_check(s[i-k])):
                count -= 1
            max_count = max(count, max_count)
        
        return max_count
        
    
    def vowel_check(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

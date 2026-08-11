class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_count = {}


        
        for char in s:
            word_count[char] = word_count.get(char, 0) + 1
            if char not in word_count:
                word[char] = 1
        
        for char in t:
            word_count[char] = word_count.get(char, 0) - 1
            if char not in word_count:
                word[char] = 1
        

        if all(values == 0 for values in word_count.values()):
            return True
        else:
            return False
        
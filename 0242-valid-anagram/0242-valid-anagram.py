class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}

        for char in s:
            word1[char] = word1.get(char, 0) + 1
            if char not in word1:
                word1[char] = 1
        
        for char in t:
            word2[char] = word2.get(char, 0) + 1
            if char not in word2:
                word2[char] = 1

        if word1 == word2:
            return True
        else:
            return False
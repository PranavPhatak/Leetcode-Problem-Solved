class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        count = []

        for char in s:
            count.append(char)

        i=0
        j=0
        while i < len(t) and j < len(count):
            if t[i] == count[j]:
                j+=1
            i += 1 

        if j == len(count):
            return True
        else:
            return False





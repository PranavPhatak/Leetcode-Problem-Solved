class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top_element = stack[-1]
                
                if (self.check_bracs(top_element, s[i])):
                    stack.pop()
                else:
                    return False
                
        if not stack:
            return True
        else:
            return False


    def check_bracs(self, top_element, open_bracket) -> bool:
        if ((open_bracket == ")" and top_element == "(") or 
            (open_bracket == "]" and top_element == "[") or
            (open_bracket == "}" and top_element == "{")):
            return True
        else:
            return False
        
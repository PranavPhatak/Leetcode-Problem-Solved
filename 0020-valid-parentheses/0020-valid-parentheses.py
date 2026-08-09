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

                if ((s[i] == ")" and top_element == "(") or 
                    (s[i] == "]" and top_element == "[") or
                    (s[i] == "}" and top_element == "{")
                ):
                    stack.pop()
                else:
                    return False
                
        if not stack:
            return True
        else:
            return False
        
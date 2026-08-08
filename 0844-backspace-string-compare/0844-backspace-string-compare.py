class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == "#" and len(stack) != 0:
                stack.pop()
            if s[i] != "#":
                stack.append(s[i])
        
        first_string = "".join(stack)
        stack.clear()

        for i in range(len(t)):
            if t[i] == "#" and len(stack) != 0:
                stack.pop()
            if t[i] != "#":
                stack.append(t[i])
        
        second_string = "".join(stack)

        return first_string == second_string
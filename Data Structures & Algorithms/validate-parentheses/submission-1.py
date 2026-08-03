class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = { "}": "{", "]":"[", ")": "("}

        for c in s:
            if c in chars: 
                # for key in chars:
                if stack and stack[-1] == chars[c]:
                #  means if stack stack is not empty, if stack[-1] = chars[value]
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False  
        # means stack empt then True otherwise false                  
        
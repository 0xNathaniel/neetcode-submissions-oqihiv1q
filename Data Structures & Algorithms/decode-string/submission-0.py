class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for c in s:
            if c.isalpha():
                current_str += c

            elif c.isdigit():
                current_num = current_num * 10 + int(c)
                
            elif c == '[':
                stack.append((current_num, current_str))
                current_num = 0
                current_str = ""

            elif c == ']':
                (old_num, old_str) = stack.pop()
                current_str = old_str + (old_num * current_str)
                current_num = 0

        return current_str
                

            
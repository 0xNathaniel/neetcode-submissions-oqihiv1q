class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current_str = ""

        # Cases for all char
        for c in path:
            if c == "/":
                if current_str == "":
                    continue

                if current_str == "..":
                    if stack:
                        stack.pop()
                    current_str = ""
                    continue

                if current_str == ".":
                    current_str = ""
                    continue

                stack.append(current_str)
                print(stack)
                current_str = ""

            else:
                current_str += c

        # Last check
        if current_str == ".." and stack:
            stack.pop()
        elif current_str != "" and current_str != ".":
            stack.append(current_str)

        return "/" +  "/".join(stack)
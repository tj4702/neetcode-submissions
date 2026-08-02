class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if char not in ['+', '-', '*', '/']:
                stack.append(int(char))
            
            else:
                a = stack.pop()
                b = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(b-a)
                elif char == '*':
                    stack.append(a*b)
                else:
                    ans = math.trunc(b/a)
                    stack.append(ans)

            # print(stack)


        return stack[-1]

        
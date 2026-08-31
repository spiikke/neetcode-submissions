class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(x)*int(y))
            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif i == "/":
                x = stack.pop()
                y = stack.pop()

                stack.append(int(float(y)/x))
            else:
                stack.append(int(i))

        return stack[0]


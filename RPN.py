# Evaluate Reverse Polish Notation : https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                elif i == '/':
                    stack.append(int(float(b) / a))
        return stack[-1]

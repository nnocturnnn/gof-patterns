import re


class Expression:
    def interpret(self, context):
        pass


class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return int(self.number)


class AddExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class SubtractExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


class Interpreter:
    token_pattern = re.compile(r"\d+|\+|-")

    def parse(self, expression):
        tokens = self.token_pattern.findall(expression)
        return self._parse_tokens(tokens)

    def _parse_tokens(self, tokens):
        stack = []
        while tokens:
            token = tokens.pop(0)
            if token.isdigit():
                stack.append(NumberExpression(token))
            elif token == "+":
                left = stack.pop()
                right = self._parse_tokens(tokens)
                return AddExpression(left, right)
            elif token == "-":
                left = stack.pop()
                right = self._parse_tokens(tokens)
                return SubtractExpression(left, right)
        return stack.pop()

    def interpret(self, expression):
        parsed_expression = self.parse(expression)
        return parsed_expression.interpret(None)


interpreter = Interpreter()
expression = "5 + 3 - 2"
result = interpreter.interpret(expression)
print(f"Result of '{expression}' is {result}")

from antlr4 import *
from SimpleDSLLexer import SimpleDSLLexer
from SimpleDSLParser import SimpleDSLParser
from SimpleDSLListener import SimpleDSLListener
import SimpleClass

class SimpleDSLCompiler(SimpleDSLListener):
    def __init__(self):
        self.variables = {}

    def enterAssignStat(self, ctx: SimpleDSLParser.AssignStatContext):
        var_name = ctx.ID().getText()
        value = self.evaluate(ctx.expr())
        self.variables[var_name] = value

    def enterPrintStat(self, ctx: SimpleDSLParser.PrintStatContext):
        value = self.evaluate(ctx.expr())
        print(value)

    def evaluate(self, ctx):
        if isinstance(ctx, SimpleDSLParser.MulDivExprContext):
            left = self.evaluate(ctx.expr(0))
            right = self.evaluate(ctx.expr(1))
            if ctx.op.type == SimpleDSLParser.MUL:
                return left * right
            else:
                return left / right
        elif isinstance(ctx, SimpleDSLParser.AddSubExprContext):
            left = self.evaluate(ctx.expr(0))
            right = self.evaluate(ctx.expr(1))
            if ctx.op.type == SimpleDSLParser.ADD:
                return left + right
            else:
                return left - right
        elif isinstance(ctx, SimpleDSLParser.IntExprContext):
            return int(ctx.INT().getText())
        elif isinstance(ctx, SimpleDSLParser.IdExprContext):
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, 0)
        else:
            return 0

def main():
    lexer = SimpleDSLLexer(FileStream('example.dsl'))
    stream = CommonTokenStream(lexer)
    parser = SimpleDSLParser(stream)
    tree = parser.prog()

    compiler = SimpleDSLCompiler()
    walker = ParseTreeWalker()
    walker.walk(compiler, tree)

if __name__ == '__main__':
    main()
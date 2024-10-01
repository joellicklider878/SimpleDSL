# Generated from SimpleDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleDSLParser import SimpleDSLParser
else:
    from SimpleDSLParser import SimpleDSLParser

# This class defines a complete listener for a parse tree produced by SimpleDSLParser.
class SimpleDSLListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleDSLParser#prog.
    def enterProg(self, ctx:SimpleDSLParser.ProgContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#prog.
    def exitProg(self, ctx:SimpleDSLParser.ProgContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#assignStat.
    def enterAssignStat(self, ctx:SimpleDSLParser.AssignStatContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#assignStat.
    def exitAssignStat(self, ctx:SimpleDSLParser.AssignStatContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#printStat.
    def enterPrintStat(self, ctx:SimpleDSLParser.PrintStatContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#printStat.
    def exitPrintStat(self, ctx:SimpleDSLParser.PrintStatContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#intExpr.
    def enterIntExpr(self, ctx:SimpleDSLParser.IntExprContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#intExpr.
    def exitIntExpr(self, ctx:SimpleDSLParser.IntExprContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#addSubExpr.
    def enterAddSubExpr(self, ctx:SimpleDSLParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#addSubExpr.
    def exitAddSubExpr(self, ctx:SimpleDSLParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:SimpleDSLParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:SimpleDSLParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SimpleDSLParser#idExpr.
    def enterIdExpr(self, ctx:SimpleDSLParser.IdExprContext):
        pass

    # Exit a parse tree produced by SimpleDSLParser#idExpr.
    def exitIdExpr(self, ctx:SimpleDSLParser.IdExprContext):
        pass



del SimpleDSLParser
# Generated from SimpleDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,42,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,1,
        2,3,2,29,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,
        1,2,0,1,4,3,0,2,4,0,2,1,0,7,8,1,0,9,10,43,0,7,1,0,0,0,2,23,1,0,0,
        0,4,28,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,
        10,1,0,0,0,10,1,1,0,0,0,11,12,5,1,0,0,12,13,5,11,0,0,13,14,5,2,0,
        0,14,15,3,4,2,0,15,16,5,3,0,0,16,24,1,0,0,0,17,18,5,4,0,0,18,19,
        5,5,0,0,19,20,3,4,2,0,20,21,5,6,0,0,21,22,5,3,0,0,22,24,1,0,0,0,
        23,11,1,0,0,0,23,17,1,0,0,0,24,3,1,0,0,0,25,26,6,2,-1,0,26,29,5,
        12,0,0,27,29,5,11,0,0,28,25,1,0,0,0,28,27,1,0,0,0,29,38,1,0,0,0,
        30,31,10,4,0,0,31,32,7,0,0,0,32,37,3,4,2,5,33,34,10,3,0,0,34,35,
        7,1,0,0,35,37,3,4,2,4,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,
        38,36,1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,5,9,23,28,
        36,38
    ]

class SimpleDSLParser ( Parser ):

    grammarFileName = "SimpleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "';'", "'print'", "'('", 
                     "')'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleDSLParser.StatContext)
            else:
                return self.getTypedRuleContext(SimpleDSLParser.StatContext,i)


        def getRuleIndex(self):
            return SimpleDSLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = SimpleDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleDSLParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleDSLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)


    class AssignStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleDSLParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleDSLParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)



    def stat(self):

        localctx = SimpleDSLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = SimpleDSLParser.AssignStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(SimpleDSLParser.T__0)
                self.state = 12
                self.match(SimpleDSLParser.ID)
                self.state = 13
                self.match(SimpleDSLParser.T__1)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(SimpleDSLParser.T__2)
                pass
            elif token in [4]:
                localctx = SimpleDSLParser.PrintStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(SimpleDSLParser.T__3)
                self.state = 18
                self.match(SimpleDSLParser.T__4)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(SimpleDSLParser.T__5)
                self.state = 21
                self.match(SimpleDSLParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleDSLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SimpleDSLParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleDSLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleDSLParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleDSLParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleDSLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleDSLParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleDSLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = SimpleDSLParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 26
                self.match(SimpleDSLParser.INT)
                pass
            elif token in [11]:
                localctx = SimpleDSLParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(SimpleDSLParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SimpleDSLParser.MulDivExprContext(self, SimpleDSLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SimpleDSLParser.AddSubExprContext(self, SimpleDSLParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expr(4)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         





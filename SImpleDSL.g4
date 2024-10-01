grammar SimpleDSL;

prog:   stat+ ;

stat:   'let' ID '=' expr ';'                # assignStat
    |   'print' '(' expr ')' ';'             # printStat
    ;

expr:   expr ('*'|'/') expr                  # mulDivExpr
    |   expr ('+'|'-') expr                  # addSubExpr
    |   INT                                 # intExpr
    |   ID                                  # idExpr
    ;

ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
WS  :   [ \t\r\n]+ -> skip ;
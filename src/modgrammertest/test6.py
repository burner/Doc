from modgrammar import *

class Number(Grammar):
	grammar = WORD("0-9")

class Operator(Grammar):
	grammar = L("+") | L("-") | L("*") | L("/")

class ParenExpr(Grammar):
	grammar = "(", REF("Expression"), ")"

class Expression(Grammar):
	grammar = Number|ParenExpr, Operator, Number|ParenExpr


parser = Expression.parser()
rslt = parser.parse_string("89 + (123 * (13123 /3))")
print(rslt.elements)

from spark import GenericScanner, GenericParser

class SimpleScanner(GenericScanner):
	def __init__(self):
		GenericScanner.__init__(self)
	
	def tokenize(self, input):
		self.rv = []
		GenericScanner.tokenize(self, input)
		return self.rv
	
	def t_whitespace(self, s):
		r' \s+ '
		pass
		
	def t_op(self, s):
		r' \+ | \* '
		self.rv.append(Token(type=s))
		
	def t_number(self, s):
		r' \d+ '
		t = Token(type='number', attr=s)
		self.rv.append(t)

class ExprParser(GenericParser):
	def __init__(self, start='expr'):
		GenericParser.__init__(self, start)
				
	def p_expr_1(self, args):
		' expr ::= expr + term '
		return AST(type=args[1],
				   left=args[0],
				   right=args[2])
		
	def p_expr_2(self, args):
		' expr ::= term '
		return args[0]
		
	def p_term_1(self, args):
		' term ::= term * factor '
		return AST(type=args[1],
				   left=args[0],
				   right=args[2])
		
	def p_term_2(self, args):
		' term ::= factor '
		return args[0]
		
	def p_factor_1(self, args):
		' factor ::= number '
		return AST(type=args[0])

	def p_factor_2(self, args):
		' factor ::= float '
		return AST(type=args[0])

def lex(inStream):
	scanner = SimpleScanner()
	return scanner.tokenize(input)

def parse(tokens):
	parser = ExprParser()
	return parser.parse(tokens)

if __name__ == "__main__":
	print("init")
	parse(lex("8234 242348 423423 + 4234 * 234234"))

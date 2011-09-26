from modgrammar import *

class MyGrammar(Grammar):
	grammar = (LITERAL("Hello,"), LITERAL("world!"))

myparser = MyGrammar.parser()
rslt = myparser.parse_string("Hello, world!")

print(rslt.elements)
print("\n\n");

class MyGrammar1(Grammar):
	grammar = (OR("Hello", "Goodbye"), ",", "world!")

myparser = MyGrammar1.parser()
rslt = myparser.parse_string("Hello, world!")
print(rslt.elements)
rslt = myparser.parse_string("Goodbye, world!")
print(rslt.elements)
print("\n\n");

class MyGrammar2(Grammar):
	grammar = (OR("Hello", "Goodbye"), ",", OPTIONAL("cruel"), "world!")

myparser = MyGrammar2.parser()
rslt = myparser.parse_string("Hello, world!")
print(rslt.elements)
rslt = myparser.parse_string("Goodbye, world!")
print(rslt.elements)
rslt = myparser.parse_string("Hello, cruel world!")
print(rslt.elements)
rslt = myparser.parse_string("Goodbye, cruel world!")
print(rslt.elements)
print("\n\n");

from modgrammar import *

class OpenWord(Grammar):
	grammar = (L("Hello") | L("Goodbye"))

class WorldPhrase(Grammar):
	grammar = (OPTIONAL(L("cruel") | L("wonderful")), "world")

class MyGrammar(Grammar):
	grammar = (OpenWord, ",", WorldPhrase, "!")

myparser = MyGrammar.parser()
rslt = myparser.parse_string("Hello, wonderful world!")
print(rslt.elements)
print(rslt[2].elements)

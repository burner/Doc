from modgrammar import *

class OpenWord(Grammar):
	grammar = (L("Hello") | L("Goodbye"))

class WorldPhrase(Grammar):
	grammar = (OPTIONAL(L("cruel") | L("wonderful")), "world")

class FirstName(Grammar):
	grammar = WORD("A-Z", "a-z")

class LastName(Grammar):
	grammar = WORD("A-Z", "a-z")

class MyNameIs(Grammar):
	grammar = ("my name is", FirstName, OPTIONAL(LastName))

class MyGrammar(Grammar):
	grammar = (OpenWord, ",", WorldPhrase | MyNameIs, "!")

myparser = MyGrammar.parser()
rslt = myparser.parse_string("Hello, wonderful world!")
print(rslt.elements)
print(isinstance(rslt[2], WorldPhrase))
print(isinstance(rslt[2], MyNameIs))
print("\n")
rslt = myparser.parse_string("Hello, my name is Robert!")
print(rslt.elements)
print(isinstance(rslt[2], WorldPhrase))
print(isinstance(rslt[2], MyNameIs))
print("\n")
rslt = myparser.parse_string("Hello, my name is Robert Schadek!")
print(rslt.elements)
print(rslt[2].elements)

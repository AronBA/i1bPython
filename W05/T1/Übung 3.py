from random import *
verben = ["Verb1","Verb2","Verb3"]
adj = ["Adj1","Adj2","Adj3"]
nomen = ["Nomen1","Nomen2","Nomen3"]


verb = choice(verben)
adjektiv = choice(adj)
nomen = choice(nomen)
satz = verb + " " +adjektiv +" "+ nomen
print(satz)
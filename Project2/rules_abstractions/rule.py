
#This is the rules_abstractions Abstraction class, to help implement custom rules_abstractions that will be defined within
# the specific rules_abstractions classes for each game.

class Rule:

    #this initializes the rules
    def __init__(self, name, machine):
        self.name = name
        self.machine = machine

    #returns true if the move is valid
    def canPlay(self):
        return

from games.egyptianratscrew import EgyptianRatScrew
import random
class AI:
    #keep track of the levels of all cards
    numAces = 0
    numTwos = 0
    numThrees = 0
    numFours = 0
    numFives = 0
    numSixes = 0
    numSevens = 0
    numEights = 0
    numNines = 0
    numTens = 0
    numJacks = 0
    numQueens = 0
    numKings = 0

    def turn(self, game):
        return game.turnIndex % len(game.players)

    def playerPrecedence(self, turn, prob, game):
        slapFreq = random.randint(0, 11)
        if (slapFreq > (slapFreq % prob)):
            game.slapQueue.enqueue(game.players[turn])
        if turn == 0: #too slow then enqueue the other
            game.slapQueue.enqueue(game.players[1])
        elif turn == 1:
            game.slapQueue.enqueue(game.players[0])

        if (game.slapQueue.notEmpty()):
            game.serviceSlap()

    def ai(self, game):

        names = ["Hanna", "Deepthi"]
        game.setPlayers(names)
        game.setEnv()
        game.begin()

        while (not isinstance(game.machine.currentState, game.machine.Win)):

            game.play()
            #calculate probability of next card played according to level of # of cards in deck
            smartness = random.randint(0,10) #how often will the AI remember the cards in the deck? 4 out of 10 times
            player = random.randint(0,1)#both have a 50 - 50 chance of being smart for any given round
            if(game.cardPlayed == None):
                continue
            if(smartness < 5):
                print("AI " + game.players[player].getName() + " is smart now.")

                if(game.cardPlayed.rank == 'K'):
                    if (self.numKings > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for face rule
                        self.playerPrecedence(player, 11, game)

                    else:
                        self.playerPrecedence(player, 6, game)
                    if (self.numKings == 4):
                        self.numKings = 0
                    self.numKings = self.numKings + 1

                elif (game.cardPlayed.rank == 'Q'):
                    if (self.numQueens > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for face rule
                        self.playerPrecedence(player, 11, game)

                    else:
                        self.playerPrecedence(player, 6, game)
                    if (self.numQueens == 4):
                        self.numQueens = 0
                    self.numQueens = self.numQueens + 1

                elif(game.cardPlayed.rank == 'J'):
                    #check probability of a double with existing levels
                    if(self.numJacks > 0): # meaning fewer in deck
                        #decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        #increase probability for face rule
                        self.playerPrecedence(player, 11, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numJacks == 4):
                        self.numJacks = 0
                    self.numJacks = self.numJacks + 1

                elif (game.cardPlayed.rank == '10'):
                    # check probability of a double with existing levels
                    if (self.numTens > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for face rule
                        self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numTens == 4):
                        self.numTens = 0
                    self.numTens = self.numTens + 1

                elif (game.cardPlayed.rank == '9'):
                    # check probability of a double with existing levels
                    if (self.numNines > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numNines == 4):
                        self.numNines = 0
                    self.numNines = self.numNines + 1

                elif (game.cardPlayed.rank == '8'):
                    # check probability of a double with existing levels
                    if (self.numEights > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numEights == 4):
                        self.numEights = 0
                    self.numEights = self.numEights + 1

                elif (game.cardPlayed.rank == '7'):
                    # check probability of a double with existing levels
                    if (self.numSevens > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numThrees > 0):
                            self.playerPrecedence(player, 2, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numSevens == 4):
                        self.numSevens = 0
                    self.numSevens = self.numSevens + 1

                elif (game.cardPlayed.rank == '6'):
                    # check probability of a double with existing levels
                    if (self.numSixes > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numFours > 0):
                            self.playerPrecedence(player, 2, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numSixes == 4):
                        self.numSixes = 0
                    self.numSixes = self.numSixes + 1

                elif (game.cardPlayed.rank == '5'):
                    # check probability of a double with existing levels
                    if (self.numFives > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numFives > 1):
                            self.playerPrecedence(player, 4, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numFives == 4):
                        self.numFives = 0
                    self.numFives = self.numFives + 1

                elif (game.cardPlayed.rank == '4'):
                    # check probability of a double with existing levels
                    if (self.numFours > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numSixes > 0):
                            self.playerPrecedence(player, 4, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numFours == 4):
                        self.numFours = 0
                    self.numFours = self.numFours + 1

                elif (game.cardPlayed.rank == '3'):
                    # check probability of a double with existing levels
                    if (self.numThrees > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numSevens > 0):
                            self.playerPrecedence(player, 4, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numThrees == 4):
                        self.numThrees = 0
                    self.numThrees = self.numThrees + 1

                elif (game.cardPlayed.rank == '2'):
                    # check probability of a double with existing levels
                    if (self.numTwos > 0):  # meaning fewer in deck
                        # decrease the probability of a slap for smart player for double rule, 10 rule, sandwich rule
                        # increase probability for 10 rule
                        if(self.numEights > 0):
                            self.playerPrecedence(player, 4, game)
                        else:
                            self.playerPrecedence(player, 7, game)
                    else:
                        self.playerPrecedence(player, 6, game)

                    if (self.numTwos == 4):
                        self.numTwos = 0
                    self.numTwos = self.numTwos + 1

                elif (game.cardPlayed.rank == 'A'):

                    self.playerPrecedence(player, 6, game)

                    if (self.numAces == 4):
                        self.numAces = 0
                    self.numAces = self.numAces + 1

#starts game.
print("____Welcome to Egyptian Rat Screw____")
print("")
print("")
game = EgyptianRatScrew()
ai = AI()
ai.ai(game)
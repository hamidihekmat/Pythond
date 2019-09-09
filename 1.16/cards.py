'''
52 - Cards
Numbered cards -> 2-10
Faced cards -> J / Q / K / A
Numbered & faced cards can have have 4 options (Hearts, Clubs, Clover, Spades)

Questions:
- how are we going to generate the cards ?
- where are we going to store these data?
- how can we tell which card has a greater value then the other card? #
{ 2: ['2 Heart', '2Club']


table types
(Hearts, Clubs, Clover, Spades) -> 1 , 2, 3, 4

table Cards
2 - 10 + J / Q / K / A (2-14) -> 11 = J , 12 = Q...

2 (1) -> 2 of Hearts
2 (2) -> 2 of Clubs
.....

This way we can easilt compare if the value is greater or less
To check who will win



ranks = { 1: 'Ace', 2 : 2 ...}

types = { 0 : 'Heats', 1...}

print(ranks[1], types[0])

'''
import random


class Cards:

    def __init__(self):
        self.ranks = {1: 'Ace', 2: 2, 3: 3, 4: 4,
                    5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                    10: 10, 11: 'Jack', 12: 'Queen', 13: 'King'}

        self.types = {0: 'Hearts', 1: 'Clubs', 2: 'Clover', 3: 'Spades'}


    def getRank(self):
        return self.ranks

    def getTypes(self):
        return self.types


class Deck(Cards):

    def __init__(self):
        Cards.__init__(self)
        self.cardDeck = []

    def generateDeck(self):
        for rank in self.ranks:
            for type in self.types:
                self.cardDeck.append([rank,type]) # vector stores type and rank

        return self.cardDeck


    def getCard(self):
        random_card = self.cardDeck[random.randint(1,53)] # workd on removing the card after it gets chosen
        return self.ranks[random_card[0]], self.types[random_card[1]]







card = Deck()
new_deck = card.generateDeck()
print(card.getCard())
print(new_deck)

# deck.py

from random import shuffle as ranshuff


class Card:

    def __init__(self, rank, suit):
        points = {'A': 1}
        nums = dict(zip(range(2, 11), range(2, 11)))
        face = {k: 10 for k in 'JQK'}
        points.update(nums)
        points.update(face)

        self.rank = rank
        self.suit = suit
        self.points = points.get(rank)

    def __repr__(self):
        return f'Card({self.rank} of {self.suit})'

    def __eq__(self, card):
        return self.rank == card.rank

    def __ne__(self, card):
        return self.rank != card.rank


class Deck:

    def __init__(self):
        ranks = ['A'] + list(range(2, 11)) + list('JQK')
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __repr__(self):
        cards = ''
        for card in self.cards:
            cards += str(card) + '\n'
        return cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def __add__(self, deck):
        return self.cards + deck.cards

    def shuffle(self):
        """
        shuffles cards in place
        """
        ranshuff(self.cards)

    def cut(self, index):
        """
        cuts the deck at index
        """
        index %= 52
        self.cards = self.cards[index:] + self.cards[:index]

    def draw(self):
        """
        pops card off top of deck
        """
        return self.cards.pop()

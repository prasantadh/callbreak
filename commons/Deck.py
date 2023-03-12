from commons.Card import Card
from commons.Suit import Suit
from commons.Rank import Rank
from random import shuffle as random_shuffle


class Deck:
    """
     _summary_

    _extended_summary_
    """

    def __init__(self):
        """
        __init__ _summary_

        _extended_summary_
        """
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        """
        shuffle _summary_

        _extended_summary_
        """
        random_shuffle(self.cards)

    def __str__(self):
        """
        __str__ _summary_

        _extended_summary_

        Returns:
            _description_
        """
        self.sort()
        return ''.join('{}{}{}'.format(
                                    card.suit,
                                    card.rank,
                                    '\n' if (idx + 1)  % 13 == 0 else '\t'
                        )
                       for idx, card in enumerate(self.cards))

    def deal(self):
        """
        deal _summary_

        _extended_summary_

        Returns:
            _description_
        """
        return self.cards.pop()

    def sort(self):
        """
        Sort the current deck such that all ranks are in descending order
        and the suits are in the order ♠, ♥, ♣, ♦.
        """
        self.cards = sorted(self.cards,
                            key=lambda card: (card.suit.value, card.rank.value),
                            reverse=True)

    def empty(self):
        return len(self.cards) == 0

if __name__ == '__main__':
    deck = Deck()
    print(deck)
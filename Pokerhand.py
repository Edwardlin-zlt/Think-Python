"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """
        Builds a histogram of the ranks that appear in the hand.
        :return: A dict of the histogram.
        """

        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """
        :return: True if the hand has a pair, False otherwise.
        """
        self.rank_hist()
        for val in self.ranks:
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """
        :return:True if the hand has two pair, False otherwise.
        """

        self.rank_hist()
        num_pair = 0
        for val in self.ranks:
            if val >= 2:
                num_pair += 1
        if num_pair >= 2:
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        """
        :return:True if the hand has a three of a kind, False otherwise.
        """

        self.rank_hist()
        for val in self.ranks:
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """
        :return: True if the hand has a straight, False otherwise.
        """

        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print hand
        print hand.has_flush()
        print ''

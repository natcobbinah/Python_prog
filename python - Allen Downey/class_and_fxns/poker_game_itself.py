from poker_cards_deck import Deck
from poker_cards_hands import Hand

class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return 
    


    def has_pair(self):
        self.suits = {}
        for card in self.cards:
            if card.suit not in self.suits:
                self.suits[card.suit] = [card.rank]
            else:
                self.suits[card.suit].append(card.rank)
        
        print(self.suits)

    def has_two_pair(self):
        pass

    def has_three_of_a_kind(self):
        pass

    def has_straight(self):
        pass

    def full_house(self):
        pass

    def four_of_a_kind(self):
        pass

    def straight_flush(self):
        pass



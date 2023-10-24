from poker_game_itself import PokerHand
from poker_cards_deck import Deck

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(1):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        #hand.sort()
        #print(hand)
        #print(hand.has_flush())
        #print('')
        print(hand.has_pair())
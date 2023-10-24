from poker_cards_deck import Deck

class Hand(Deck):
    """
    Represents a hand of playing cards
    """
    def __init__(self, label = ''):
        self.cards = []
        self.label = label

    def find_defining_class(obj, meth_name):
        for ty in type(obj).mro():
            if meth_name in ty.__dict__:
                return ty

#deck = Deck()
#print(deck)
#hand1 = Hand('Hand One')
#hand2 = Hand('Hand Two')


#dealt_hands = deck.deal_hands(hand1,hand2,5)
#for cards in dealt_hands:
#    print(cards)

#print(hand1.find_defining_class('shuffle'))
#hand.add_card(card)
#print(hand)
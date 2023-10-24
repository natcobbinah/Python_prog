from poker_cards import Card

import random

class Deck:
    
    def __init__(self):
        self.cards = []

        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_card(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    # exercise
    def deal_hands(self, hand1, hand2, num_of_cards_per_hand):

        list_of_hands = []
        self.shuffle()

        for i in range(num_of_cards_per_hand):
            hand1.add_card(self.pop_card())
        list_of_hands.append(f"hand1\n{hand1}")

        for i in range(num_of_cards_per_hand):
            hand2.add_card(self.pop_card())
        list_of_hands.append(f"hand2\n{hand2}")
        
        return list_of_hands
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
#deck = Deck()
#print(deck)
from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re


class MyHandCards(IAlterationEntity):
    # Needs only Zone
    hand_cards = []

    def __init__(self):
        self.hand_cards = []

    def debug_print_shit(self):
        print "******************"
        rows = [[str(item.name), str(item.attack), "\\", str(item.health), " manacost: ", str(item.mana_cost)] for item
                in self.hand_cards]
        widths = [max(map(len, col)) for col in zip(*rows)]
        for row in rows:
            print "  ".join((val.ljust(width) for val, width in zip(row, widths)))

    def add_card_to_hand(self, card):
        self.hand_cards.append(card)

    def del_card_from_hand(self, special_id):
        self.hand_cards = [card for card in self.hand_cards if card.special_id != special_id]

    def change_card_position(self, special_id, new_pos):
        temp_card = next((card for card in self.hand_cards if card.special_id == special_id), None)
        if temp_card == None:
            return
        self.hand_cards.remove(temp_card)
        self.hand_cards.insert(new_pos - 1, temp_card)

    def tag_change(self, tag_name, value, special_id):
        card_pos = None
        for i in range(0, len(self.hand_cards)):
            if self.hand_cards[i].special_id == special_id:
                card_pos = i
        if card_pos == None:
            return
        if tag_name == "ATK":
            self.hand_cards[card_pos].attack = int(value)
        if tag_name == "HEALTH":
            self.hand_cards[card_pos].health = int(value)
        if tag_name == "TAG_LAST_KNOWN_COST_IN_HAND":
            self.hand_cards[card_pos].mana_cost = int(value)

    def check_n_change(self, logLine):
        played_card = re.search(regExps.from_friendly_hand, logLine)
        drawed_card = re.search(regExps.to_friendly_hand, logLine)
        changed_position = re.search(regExps.change_card_position, logLine)
        tag_change = re.search(regExps.tag_change, logLine)
        if played_card:
            self.del_card_from_hand(int(played_card.group("id")))
        if drawed_card:
            self.add_card_to_hand(Card(drawed_card.group("cardId"), int(drawed_card.group("id"))))
        if changed_position:
            self.change_card_position(int(changed_position.group("id")), int(changed_position.group("pos_2")))
        if tag_change:
            self.tag_change(tag_change.group("tag"), tag_change.group("value"), int(tag_change.group("id")))


class OpponentHandCards(IAlterationEntity):
    # Needs only Zone
    num_of_cards = int

    def __init__(self):
        self.num_of_cards = 0

    def debug_print_shit(self):
        print self.num_of_cards

    def check_n_change(self, logLine):
        to_hand = re.search(regExps.to_opposing_hand, logLine)
        from_hand = re.search(regExps.from_opposing_hand, logLine)
        if to_hand:
            self.num_of_cards += 1
        if from_hand:
            self.num_of_cards -= 1
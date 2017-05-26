from Parser import Parser
from HSActions import HSActions
import time

parser = Parser()
actions = HSActions()


def mulligan(my_hand):
    for i in range(0, len(my_hand.hand_cards)):
        if my_hand.hand_cards[i].mana_cost >= 3:
            actions.mulligan_card(my_hand, i + 1)


def find_card_to_play(my_hand, available_resources):
    for i in range(0, len(my_hand.hand_cards)):
        if my_hand.hand_cards[i].mana_cost <= available_resources and my_hand.hand_cards[i].type == "WEAPON":
            return i
    for i in range(0, len(my_hand.hand_cards)):
        if my_hand.hand_cards[i].mana_cost <= available_resources:
            return i
    return None


def find_taunt(opp_board):
    for i in range(1, opp_board.size_minions() + 1):
        if opp_board.minions[i].taunt:
            return i
    return None


def find_non_exhausted_minion(my_board):
    for i in range(1, my_board.size_minions() + 1):
        if int(my_board.minions[i].exhausted) == 0 and my_board.minions[i].attack > 0:
            my_board.minions[i].exhausted = 1
            return i
    if parser.my_hero.exhausted == False and parser.my_hero.atk > 0:
        return 0
    return None

parser.start()

while True:
    time.sleep(5)
    actions.find_next_game()

    while parser.game_state.game_state != 0:
        time.sleep(2)

    time.sleep(20)
    mulligan(parser.my_hand)
    actions.confirm_mulligan()
    time.sleep(10)

    while parser.game_state.game_state != 4:
        if parser.game_state.game_state == 1:
            time.sleep(3)
            num_of_card = find_card_to_play(parser.my_hand, parser.my_hero.available_resources)
            while num_of_card != None:
               if len(parser.my_hand.hand_cards) > 0 and parser.my_hand.hand_cards[num_of_card].type == "WEAPON":
                   actions.play_weapon(parser.my_hand, num_of_card + 1)
               if len(parser.my_hand.hand_cards) > 0 and parser.my_hand.hand_cards[num_of_card].type == "SPELL":
                   actions.play_spell(parser.my_hand, num_of_card + 1, 0 if parser.my_hand.hand_cards[num_of_card].target_required else None, parser.my_board, parser.opp_board)
               if len(parser.my_hand.hand_cards) > 0 and parser.my_hand.hand_cards[num_of_card].type == "MINION":
                   actions.play_minion(parser.my_hand, num_of_card + 1, 1, None, parser.my_board, parser.opp_board)
               time.sleep(3)
               num_of_card = find_card_to_play(parser.my_hand, parser.my_hero.available_resources)
            if parser.my_hero.available_resources >= 2:
                actions.hero_power(None, parser.opp_board)
            time.sleep(8)
            taunt_id = find_taunt(parser.opp_board)
            minion_to_hit = find_non_exhausted_minion(parser.my_board)
            while minion_to_hit != None:
                if taunt_id == None:
                    actions.hit(minion_to_hit, 0, parser.my_board.size_minions(), parser.opp_board.size_minions())
                if taunt_id != None:
                    actions.hit(minion_to_hit, taunt_id, parser.my_board.size_minions(), parser.opp_board.size_minions())
                time.sleep(5)
                taunt_id = find_taunt(parser.opp_board)
                minion_to_hit = find_non_exhausted_minion(parser.my_board)
            time.sleep(2)
            actions.end_turn()
            time.sleep(8)
        time.sleep(3)
    actions.after_game_over()
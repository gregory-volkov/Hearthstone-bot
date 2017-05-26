from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re


class GameState(IAlterationEntity):
    __scha_budet__ = bool
    game_state = int
    mulligan_ended = bool
    # 0 - Mulligan
    # 1 - Your turn
    # 2 - Opponent turn
    # 3 - Discovering
    # 4 - Game ended
    # 5 - Game started

    def __init__(self):
        self.game_state = 4
        self.__waiting_4_deck__ = False
        self.mulligan_ended = False

    def debug_print_shit(self):
        print "gamestate: " + str(self.game_state)

    def check_n_change(self, logLine):
        mulligan = re.search(regExps.end_of_mulligan, logLine)
        main_action_start = re.search(regExps.main_action_start, logLine)
        game_over = re.search(regExps.game_over, logLine)
        game_created = re.search(regExps.game_started, logLine)
        if mulligan:
            self.mulligan_ended = True
            return
        if main_action_start:
            self.__waiting_4_deck__ = True
            return
        my_turn = re.search(regExps.waiting_4_friendly_deck, logLine)
        opp_turn = re.search(regExps.waiting_4_opposing_deck, logLine)
        if my_turn and self.mulligan_ended:
            self.game_state = 1
            self.__waiting_4_deck__ = False
        if opp_turn and self.mulligan_ended:
            self.game_state = 2
            self.__waiting_4_deck__ = False
        if game_over:
            self.game_state = 4
        if game_created:
            self.game_state = 0
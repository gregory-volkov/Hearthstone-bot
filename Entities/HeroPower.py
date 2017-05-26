from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re
import PlayersInfo


class MyHeroPower(IAlterationEntity):
    # Needs Power
    is_available = bool
    players_info = PlayersInfo

    def debug_print_shit(self):
        print "my heropower " + str(self.is_available)

    def __init__(self, players_info):
        self.is_available = True
        self.players_info = players_info

    def check_n_change(self, logLine):
        num_of_activations_this_turn = re.search(regExps.hero_power_activations.replace("(name)", self.players_info.my_name), logLine)
        if num_of_activations_this_turn:
            self.is_available = True if int(num_of_activations_this_turn.group("value")) == 0 else False


class OpponentHeroPower(IAlterationEntity):
    # Needs Power
    is_available = bool
    players_info = PlayersInfo

    def debug_print_shit(self):
        print "opponent heropower " + str(self.is_available)

    def __init__(self, players_info):
        self.is_available = True
        self.players_info = players_info

    def check_n_change(self, logLine):
        num_of_activations_this_turn = re.search(regExps.hero_power_activations.replace("(name)", self.players_info.opp_name), logLine)
        if num_of_activations_this_turn:
            self.is_available = True if int(num_of_activations_this_turn.group("value")) == 0 else False
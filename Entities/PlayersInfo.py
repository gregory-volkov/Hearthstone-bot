from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re


class PlayersInfo(IAlterationEntity):
    # Needs Zone
    my_id = int
    my_name = str
    opp_id = int
    opp_name = str
    my_player_num = int
    opposing_player_num = int
    __waiting_for_opp_name__ = bool

    def __init__(self):
        self.__waiting_for_opp_name__ = False
        self.my_name = ""
        self.opp_name = ""

    def debug_print_shit(self):
        print "My name: " + self.my_name
        print "Opponent name: " + self.opp_name
        print "My num: " + str(self.my_player_num)
        print "Opp num: " + str(self.opposing_player_num)

    def check_n_change(self, logLine):
        to_friendly_hand = re.search(regExps.smth_to_friendly_hand, logLine)
        to_opposing_hand = re.search(regExps.smth_to_opposing_hand, logLine)
        player_name_n_id = re.search(regExps.player_name_n_id, logLine)
        my_player_num = re.search(regExps.who_is_who1, logLine)
        opp_player_num = re.search(regExps.who_is_who2, logLine)
        if to_friendly_hand:
            self.__waiting_for_opp_name__ = False
        if to_opposing_hand:
            self.__waiting_for_opp_name__ = True
        if player_name_n_id and self.__waiting_for_opp_name__:
            self.opp_id = player_name_n_id.group("id")
        if player_name_n_id and not(self.__waiting_for_opp_name__):
            self.my_id = player_name_n_id.group("id")
            self.my_name = player_name_n_id.group("name")
        if my_player_num:
            self.my_player_num = my_player_num.group("player_numb")
        if opp_player_num:
            self.opposing_player_num = opp_player_num.group("player_numb")
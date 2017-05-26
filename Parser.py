import time
from Entities import *
import os
import threading

class Parser():

    def __init__(self):
        pass

    def init_entities(self):
        self.my_hand = Hand.MyHandCards()
        self.opp_hand = Hand.OpponentHandCards()
        self.players_info = PlayersInfo.PlayersInfo()
        self.my_hero_power = HeroPower.MyHeroPower(self.players_info)
        self.opp_hero_power = HeroPower.OpponentHeroPower(self.players_info)
        self.my_board = Board.Board(0)
        self.opp_board = Board.Board(1)
        self.game_state = GameState.GameState()
        self.my_hero = Hero.MyHero(self.players_info)

    def deleteContent(self, fName):
        with open(fName, "w"):
            pass

    def start(self):
        self.init_entities()
        parser_thread = threading.Thread(target=self.main)
        parser_thread.start()

    def main(self):
        power_filename = 'C:\Program Files (x86)\Hearthstone\Logs\Power.log'
        zone_filename = 'C:\Program Files (x86)\Hearthstone\Logs\Zone.log'
        try:
            self.deleteContent(power_filename)
            self.deleteContent(zone_filename)
        finally:
            pass

        zone = open(zone_filename,'r')
        zone.seek(os.stat(zone_filename)[6])

        power = open(power_filename, 'r')
        power.seek(os.stat(power_filename)[6])

        while True:
            if self.game_state.game_state == 4:
                self.init_entities()
            where_power = power.tell()
            where_zone = zone.tell()
            log_line = zone.readline() + power.readline()
            if not log_line:
                time.sleep(0.5)
            else:
                self.my_hand.check_n_change(log_line)
                self.opp_hand.check_n_change(log_line)
                self.players_info.check_n_change(log_line)
                self.my_hero_power.check_n_change(log_line)
                self.opp_hero_power.check_n_change(log_line)
                self.my_board.check_n_change(log_line)
                self.opp_board.check_n_change(log_line)
                self.game_state.check_n_change(log_line)
                self.my_hero.check_n_change(log_line)
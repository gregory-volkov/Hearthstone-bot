from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re
import PlayersInfo


class MyHero(IAlterationEntity):
    players_info = PlayersInfo
    hp = int
    armor = int
    has_weapon = bool
    exhausted = bool
    mana_crystals = int
    available_resources = int
    __temp_resources__ = int
    __resources_used__ = int
    __prepare_damage__ = bool
    atk = int

    def __init__(self, players_info):
        self.hp = 30
        self.players_info = players_info
        self.__temp_resources__ = 0
        self.__prepare_damage__ = False
        self.__resources_used__ = 0
        self.has_weapon = False
        self.exhausted = False
        self.atk = 0

    def debug_print_shit(self):
        print "HP: " + str(self.hp) + " Mana: " + str(self.available_resources)

    def change_resource(self, tag_name, entity, value):
        if entity == self.players_info.my_name:
            if tag_name == "TEMP_RESOURCES":
                self.__temp_resources__ = value
                self.available_resources = self.mana_crystals + value - self.__resources_used__
            if tag_name == "RESOURCES":
                self.mana_crystals = value
                self.available_resources = value
            if tag_name == "RESOURCES_USED":
                self.__resources_used__ = value
                self.available_resources = self.mana_crystals + self.__temp_resources__ - value

    def check_n_change(self, logLine):
        resources_changed = re.search(regExps.resources_tag_change, logLine)
        damage_changed = re.search(regExps.hero_damaged_tag.replace("(player_num)", str(self.players_info.my_player_num)), logLine)
        exhausted_tag_change = re.search(regExps.hero_exhausted.replace("player_num", str(self.players_info.my_player_num)), logLine)
        weapon_added = re.search(regExps.my_weapon_played, logLine)
        weapon_dead = re.search(regExps.my_weapon_dead, logLine)
        atk_changed = re.search(regExps.hero_atk_change.replace("player_num", str(self.players_info.my_player_num)), logLine)
        if damage_changed:
            self.hp = 30 - int(damage_changed.group("value"))
        if resources_changed and resources_changed.group("value") != "":
            self.change_resource(resources_changed.group("tag"), resources_changed.group("name"), int(resources_changed.group("value")))
        if exhausted_tag_change:
            self.exhausted = True if int(exhausted_tag_change.group("value")) == 1 else False
        if weapon_added:
            self.has_weapon = True
        if weapon_dead:
            self.has_weapon = False
        if atk_changed:
            self.atk = int(atk_changed.group("value"))
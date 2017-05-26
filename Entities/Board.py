from Interfaces import IAlterationEntity
from Classes import *
from RegExps import *
import re


class Board(IAlterationEntity):
    minions = [Minion(None, None)] * 10
    playerNumb = 0
    isOpponent = 0

    def __init__(self, t):
        self.minions = [Minion(None, None)] * 10
        self.isOpponent = t

    def size_minions(self):
        i = 0
        for j in self.minions:
            if (j.name != None):
                i += 1
        return i

    def addMinion(self, minion, dstPos):
        if minion.type != "MINION":
            return
        dstPos = int(dstPos)
        if dstPos == len(self.minions) or dstPos == 0:
            self.minions[dstPos] = minion
        else:
            for i in range(7, dstPos, -1):
                self.minions[i] = self.minions[i - 1]
            self.minions[dstPos] = minion

    def get_minion_index_by_id(self, special_id):
        for i in range(len(self.minions)):
            if isinstance(self.minions[i], Minion) and self.minions[i].special_id == special_id:
                return i
                break
        else:
            return None

    def getMinionIndex(self, minion):
        return self.get_minion_index_by_id(minion.special_id)

    def removeMinionByIndex(self, index):
        if index == None:
            return
        if index == 0:
            self.minions[index] = Minion(None, None)
            return
        for i in range(index, 7):
            self.minions[i] = self.minions[i + 1]
        self.minions[7] = Minion(None, None)

    def removeMinion(self, minion):
        self.removeMinionByIndex(self.getMinionIndex(minion))

    def debug_print_shit(self):
        print "******************"
        rows = [[str(self.minions[i].name), str(self.minions[i].special_id), str(self.minions[i].attack), "/",
                 str(self.minions[i].health), str(self.minions[i].exhausted), str(self.minions[i].frozen)] for i in
                range(len(self.minions))]
        widths = [max(map(len, col)) for col in zip(*rows)]
        for row in rows:
            print "  ".join((val.ljust(width) for val, width in zip(row, widths)))

    def change_position(self, special_id, dstPos):
        ti = self.get_minion_index_by_id(special_id)
        if ti == None:
            return
        t = self.minions[ti]
        if t == None:
            return
        self.removeMinionByIndex(ti)
        self.addMinion(t, dstPos)

    def change_minion_tag(self, special_id, tag, value):
        ti = self.get_minion_index_by_id(special_id)
        if ti == None:
            return
        t = self.minions[ti]
        if (tag == "TAUNT"):
            self.minions[ti].add_mechanic(tag)
            self.minions[ti].update_mechanics()
        if (tag == "ZONE" and value == "SETASIDE"):
            self.removeMinionByIndex(ti)
        if (tag == "EXHAUSTED"):
            self.minions[ti].exhausted = value
        if (tag == "ATK"):
            self.minions[ti].attack = value
        if (tag == "DAMAGE"):
            self.minions[ti].health = self.minions[ti].maxHealth - int(value)
        if (tag == "FROZEN"):
            self.minions[ti].frozen = value
        if (tag == "CHARGE"):
            self.minions[ti].charge = value
            if int(self.minions[ti].just_played) == 1 and int(self.minions[ti].charge) == 1:
                self.minions[ti].exhausted = 0
        if (tag == "JUST_PLAYED"):
            self.minions[ti].just_played = value

    def check_n_change(self, logLine):
        friendlyMinionPlay = re.search(regExps.friendly_minion_play2, logLine)
        minionChangePosition = re.search(regExps.minion_change_position2, logLine)
        oppositeMinionPlay = re.search(regExps.opposite_minion_play, logLine)
        died = re.search(regExps.died, logLine)
        whoIsWho1 = re.search(regExps.who_is_who1, logLine)
        whoIsWho2 = re.search(regExps.who_is_who2, logLine)
        MiniontagChanged1 = re.search(regExps.minion_tag_changed1, logLine)
        MiniontagChanged2 = re.search(regExps.minion_tag_changed2, logLine)
        if MiniontagChanged1:
            self.change_minion_tag(MiniontagChanged1.group("id"), MiniontagChanged1.group("tag"),
                                   MiniontagChanged1.group("value"))
        if MiniontagChanged2:
            self.change_minion_tag(MiniontagChanged2.group("id"), MiniontagChanged2.group("tag"),
                                   MiniontagChanged2.group("value"))

        if whoIsWho1 and self.isOpponent == 0:
            self.playerNumb = int(whoIsWho1.group("player_numb"))
        if whoIsWho2 and self.isOpponent == 1:
            self.playerNumb = int(whoIsWho2.group("player_numb"))
        if died:
            self.removeMinion(Minion(died.group("cardId"), (died.group("id"))))
        if friendlyMinionPlay and self.isOpponent == 0:
            self.addMinion(Minion(friendlyMinionPlay.group("cardId"), friendlyMinionPlay.group("id")),
                           friendlyMinionPlay.group("dstPos"))
        if oppositeMinionPlay and self.isOpponent == 1:
            self.addMinion(Minion(oppositeMinionPlay.group("cardId"), oppositeMinionPlay.group("id")),
                           oppositeMinionPlay.group("dstPos"))
        if minionChangePosition and self.playerNumb == int(minionChangePosition.group("player")):
            self.change_position(minionChangePosition.group("id"), int(minionChangePosition.group("dstPos")))
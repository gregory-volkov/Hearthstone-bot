import json

with open('cards.json') as data_file:
    cards = json.load(data_file)


def json_id_by_cardId(cardId):
    for i in range(0, len(cards)):
        if cards[i]["id"] == cardId:
            return i
    return 0

def get_json_prop(cardId, prop):
    t = json_id_by_cardId(cardId)
    if prop in cards[t]:
        return cards[t][prop]
    else:
        return None


class Card():
    card_id = None #str
    mana_cost  = None #int
    special_id = None #int
    name       = None #str
    type       = None #str
    attack     = None #int
    health     = None #int
    json_num   = None #str
    target_required = None #bool

    def __init__(self, cardId, specialId):
        self.special_id = specialId
        self.card_id    = cardId
        self.json_num   = json_id_by_cardId(cardId)
        self.name       = get_json_prop(cardId, "name")
        self.type       = get_json_prop(cardId, "type")
        self.attack     = get_json_prop(cardId, "attack")
        self.health     = get_json_prop(cardId, "health")
        self.mana_cost  = get_json_prop(cardId, "cost")
        if get_json_prop(cardId, "playRequirements") != None:
            self.target_required = True if "REQ_TARGET_TO_PLAY" in get_json_prop(cardId, "playRequirements") else False
        else:
            self.target_required = False


class Minion(Card):
    name = None  # str
    card_id = None  # int
    special_id = None  # int
    json_num = None  # str
    attack = None  # int
    health = None  # int
    maxHealth = None  # int
    isMine = None  # bool
    silenced = None  # bool
    windfury = None  # bool
    taunt = None  # bool
    divine_shield = None  # bool
    frozen = None  # bool
    stealth = None  # bool
    position = None  # int
    num_attacks_this_turn = None  # int
    poisonous = None  # bool
    cost = None  # int
    charge = 0
    just_played = 0
    exhausted = 0  # bool


    mechanics = []

    def __init__(self, cardId, specialId):
        self.type = get_json_prop(cardId, "type")
        if (self.type == "MINION"):
            self.special_id = specialId
            self.card_id = cardId
            self.json_num = json_id_by_cardId(cardId)
            self.name = get_json_prop(cardId, "name")
            self.attack = get_json_prop(cardId, "attack")
            self.health = get_json_prop(cardId, "health")
            self.maxHealth = get_json_prop(cardId, "health")
            self.exhausted = 0
            self.frozen = 0
            self.mechanics = get_json_prop(cardId, "mechanics")
            if (self.mechanics == None):
                self.mechanics = []
            self.update_mechanics()
            self.charge = 0
            self.just_played = 0

    def update_mechanics(self):
        if self.mechanics != None and "TAUNT" in self.mechanics:
            self.taunt = 1

    def check_mechanic(self, mech):
        return mech in self.mechanics

    def add_mechanic(self, mech):
        self.mechanics += [mech]

    def delete_mechanic(self, mech):
        self.mechanics.remove(mech)
        
        
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
class Rect:
    def __init__(self, (left, top, right, bottom)):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
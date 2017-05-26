import BaseActions


def PlayMinion(my_hand, num_of_card, position, num_of_target, my_board, opp_board):
    BaseActions.MoveToCard(len(my_hand.hand_cards), num_of_card)
    BaseActions.SendClick()
    BaseActions.MoveBetweenMinions(my_board.size_minions(), position)
    BaseActions.SendClick()
    if num_of_target != None:
        BaseActions.MoveToOpponentMinion(opp_board.size_minions(), num_of_target)
        BaseActions.SendClick()


def PlaySpell(my_hand, num_of_card, num_of_target, my_board, opp_board):
    BaseActions.MoveToCard(len(my_hand.hand_cards), num_of_card)
    BaseActions.SendClick()
    if num_of_target != None:
        BaseActions.MoveToOpponentMinion(opp_board.size_minions(), num_of_target)
        BaseActions.SendClick()
    else:
        BaseActions.MoveToBattleField()
        BaseActions.SendClick()


def PlayWeapon(my_hand, num_of_card):
    BaseActions.MoveToCard(len(my_hand.hand_cards), num_of_card)
    BaseActions.SendClick()
    BaseActions.MoveToBattleField()
    BaseActions.SendClick()
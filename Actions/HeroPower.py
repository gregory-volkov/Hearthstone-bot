import BaseActions


def HeroPower(target, opp_board):
    BaseActions.MoveTo(60, 76)
    BaseActions.SendClick()
    if target != None:
        BaseActions.MoveToOpponentMinion(opp_board.size_minions(), target)
        BaseActions.SendClick()
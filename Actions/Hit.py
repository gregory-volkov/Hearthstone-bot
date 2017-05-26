import BaseActions


def HitMinion(minionNum, targetNum, myBoardSize, oppBoardSize):
    BaseActions.MoveToMinion(myBoardSize, minionNum)
    BaseActions.SendClick()
    BaseActions.MoveToOpponentMinion(oppBoardSize, targetNum)
    BaseActions.SendClick()

def Hit(myMinion, oppMinion, myBoard, oppBoard):
    BaseActions.MoveToMinion(myBoard.size_minions(), myBoard.get_minion_index_by_id(myMinion.special_id))
    BaseActions.SendClick()
    BaseActions.MoveToOpponentMinion(oppBoard.size_minions(), oppBoard.get_minion_index_by_id(oppMinion.special_id))
    BaseActions.SendClick()
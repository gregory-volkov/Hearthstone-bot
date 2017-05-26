import BaseActions
import time
import itertools


def ReturnToDeckPick():
    BaseActions.MoveTo(81,83)
    for _ in itertools.repeat(None, 10):
        BaseActions.SendClick()
        time.sleep(1)
import BaseActions


def ConfirmMulligan():
    BaseActions.MoveTo(49, 80)
    BaseActions.SendClick()

def Mulligan(my_hand, cardNum):
    isCoin = False
    for card in my_hand.hand_cards:
        if card.name == "The Coin":
            isCoin = True
    if not isCoin:
        optionSize = 24.5
        optionsWidth = 3 * optionSize
        myOption = (cardNum * optionSize) - (optionSize / 2)
        optionStart = 50 - (optionsWidth / 2)
        BaseActions.MoveTo(optionStart + myOption, 50)
        BaseActions.SendClick()
    else:
        optionSize = 17.5
        optionsWidth = 4 * optionSize
        myOption = (cardNum * optionSize) - (optionSize / 2)
        optionStart = 50 - (optionsWidth / 2)
        BaseActions.MoveTo(optionStart + myOption, 50)
        BaseActions.SendClick()
from Actions import *
import time


class HSActions():
    def end_turn(self):
        EndTurn.EndTurn()

    def after_game_over(self):
        AfterGameOver.ReturnToDeckPick()

    def play_minion(self, my_hand, num_of_card, position, num_of_target, my_board, opp_board):
        PlayingCards.PlayMinion(my_hand, num_of_card, position, num_of_target, my_board, opp_board)

    def play_spell(self, my_hand, num_of_card, num_of_target, my_board, opp_board):
        PlayingCards.PlaySpell(my_hand, num_of_card, num_of_target, my_board, opp_board)

    def hero_power(self, target, opp_board):
        HeroPower.HeroPower(target, opp_board)

    def hit(self, minionNum, targetNum, myBoardSize, oppBoardSize):
        Hit.HitMinion(minionNum, targetNum, myBoardSize, oppBoardSize)

    def confirm_mulligan(self):
        Mulligan.ConfirmMulligan()

    def mulligan_card(self, my_hand, card_num):
        Mulligan.Mulligan(my_hand, card_num)

    def find_next_game(self):
        FindNextGame.FindNextGame()

    def play_weapon(self, my_hand, num_of_card):
        PlayingCards.PlayWeapon(my_hand, num_of_card)
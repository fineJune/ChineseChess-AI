# -*-coding:utf-8-*-

"""
@author cc
@date 2021/2/17
"""

import config
import rule

import json


class Board:
    def __init__(self):
        self._board = []
        self.status = False
        self.roundGame = 0
        self.boardInit()
        self.moveSet = []

        self.boardRecoder = []

   

    def boardInit(self):
        self._board = config.__BOARD_INIT__.copy()
        self.checkedStoneID = config.__UNCKECKED__
        self.currentPlayer = 'RED'

    def getBoard(self):
        return self._board

    def getStoneFromID(self, id):
        stone = self._board[id]
        if stone == config.b_兵:
            return "卒"
        elif stone == config.b_炮:
            return "炮"
        elif stone == config.b_车:
            return "车"
        elif stone == config.b_马:
            return "马"
        elif stone == config.b_相:
            return "象"
        elif stone == config.b_士:
            return "士"
        elif stone == config.b_将:
            return "将"
        elif stone == config.r_兵:
            return "兵"
        elif stone == config.r_炮:
            return "炮"
        elif stone == config.r_车:
            return "车"
        elif stone == config.r_马:
            return "马"
        elif stone == config.r_相:
            return "相"
        elif stone == config.r_士:
            return "仕"
        elif stone == config.r_将:
            return "帅"

    def setChecked(self, id):
        self.checkedStoneID = id

    def changePlayer(self):
        # print("换边")
        if 'red' in self.currentPlayer.lower():
            self.currentPlayer = 'BLACK'
        else:
            self.currentPlayer = 'RED'

    def whichPlayer(self, stone):
        if stone == config.__BLANK__:
            return 'BLANK'
        #     return 'BLACK' if 'red' in self.currentPlayer else 'RED'
        elif config.b_兵 <= stone <= config.b_将:
            return "BLACK"
        else:
            return "RED"

    def move(self, ido, idd):
        self.boardRecoder.append(self._board.copy())
        if self.whichPlayer(self._board[idd]) != self.whichPlayer(self._board[ido]) and 'BLANK' not in self.whichPlayer(self._board[ido]):
            self._board[ido], self._board[idd] = config.__BLANK__, self._board[ido]
        else:
            self._board[ido], self._board[idd] = self._board[idd], self._board[ido]


        self.checkedStoneID = config.__UNCKECKED__
        self.changePlayer()


    def canMove(self, id):
        if self.status:
            return

        if self._board[self.checkedStoneID] == config.r_兵 or self._board[self.checkedStoneID] == config.b_兵:
            # print("移动兵")
            # TODO 兵走法
            return rule.canMoveBING(self.checkedStoneID, id, self)
        elif self._board[self.checkedStoneID] == config.r_炮 or self._board[self.checkedStoneID] == config.b_炮:
            # TODO 炮走法
            # print("移动炮")
            return rule.canMovePAO(self.checkedStoneID, id, self)

        elif self._board[self.checkedStoneID] == config.r_车 or self._board[self.checkedStoneID] == config.b_车:
            # print("移动车")
            return rule.canMoveCHE(self.checkedStoneID, id, self)
            # TODO 车走法
        elif self._board[self.checkedStoneID] == config.r_相 or self._board[self.checkedStoneID] == config.b_相:
            # print("移动相")
            return rule.canMoveXIANG(self.checkedStoneID, id, self)
            # TODO 相走法
        elif self._board[self.checkedStoneID] == config.r_士 or self._board[self.checkedStoneID] == config.b_士:
            # print("移动士")
            return rule.canMoveSHI(self.checkedStoneID, id, self)
            # TODO 士走法
        elif self._board[self.checkedStoneID] == config.r_将 or self._board[self.checkedStoneID] == config.b_将:
            # print("移动将")
            return rule.canMoveJIANG(self.checkedStoneID, id, self)
            # TODO 将走法
        elif self._board[self.checkedStoneID] == config.r_马 or self._board[self.checkedStoneID] == config.b_马:
            # print("移动马")
            return rule.canMoveMA(self.checkedStoneID, id, self)
            # TODO 马走法



    def getMove(self, move):
        ido = (int(move[0])) + (int(move[1])) * 9
        idd = (int(move[2])) + (int(move[3])) * 9
        return ido, idd

    def returnHash(self):
        return ''.join([str(i) for i in self._board])

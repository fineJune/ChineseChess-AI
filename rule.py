# -*-coding:utf-8-*-

"""
@author cc
@date 2021/2/17
@func rule set define
"""

import func, config


def getStoneCountX(xo, xd, board):
    count = 0
    xo, xd = min(xo, xd), max(xo, xd)
    for i in range(xo + 1, xd, 1):
        if board[i] != config.__BLANK__:
            count += 1
    # print("水平", count)
    return count


def getStoneCountY(xo, xd, board):
    count = 0
    xo, xd = min(xo, xd), max(xo, xd)
    for i in range(xo + 9, xd, 9):
        if board[i] != config.__BLANK__:
            count += 1
    # print("竖直", count)
    return count


def stillSameSide(id, stone):
    return (id >= (len(config.__BOARD_INIT__) - 1) / 2 and stone <= config.r_将) or (
            id <= (len(config.__BOARD_INIT__) - 1) / 2 and stone >= config.b_兵)


def isPin(id, board):
    if 0 > id or id >= len(board):
        return False
    return board[id] == config.__BLANK__


def canMoveBING(ido, idd, board):
    typeStone = board.whichPlayer(board.getBoard()[ido]).lower()

    if stillSameSide(ido, board.getBoard()[ido]):
        # print("未过河")
        if 'red' in typeStone:
            return idd - ido in config.__LEGAL_红兵_MOVE_SET__
        elif 'black' in typeStone:
            return idd - ido in config.__LEGAL_黑兵_MOVE_SET__
    else:
        if 'red' in typeStone:
            return idd - ido in config.__LEGAL_红兵_过河_MOVE_SET__
        elif 'black' in typeStone:
            return idd - ido in config.__LEGAL_黑兵_过河_MOVE_SET__


def canMoveXIANG(ido, idd, board):
    return idd - ido in config.__LEGAL_相_MOVE_SET__ and isPin(
        ido + config.__PIN_相__[config.__LEGAL_相_MOVE_SET__.index(idd - ido)], board.getBoard()) and stillSameSide(idd,
                                                                                                                  board.getBoard()[
                                                                                                                      ido])


def canMoveMA(ido, idd, board):
    # print(config.__PIN_马__[int(config.__LEGAL_马_MOVE_SET__.index(idd - ido) / 2)])
    return idd - ido in config.__LEGAL_马_MOVE_SET__ and isPin(
        ido + config.__PIN_马__[int(config.__LEGAL_马_MOVE_SET__.index(idd - ido) / 2)], board.getBoard())


def canMovePAO(ido, idd, board):
    if int(ido / 9) == int(idd / 9):
        return (getStoneCountX(ido, idd, board.getBoard()) == 0 and board.getBoard()[idd] == config.__BLANK__) or (
                getStoneCountX(ido, idd, board.getBoard()) == 1 and (
                (board.whichPlayer(board.getBoard()[idd]) != board.whichPlayer(
            board.getBoard()[ido]) and (board.getBoard()[idd] != config.__BLANK__))))
    elif 0 == (abs(ido - idd) % 9):
        return (getStoneCountY(ido, idd, board.getBoard()) == 0 and board.getBoard()[idd] == config.__BLANK__) or (
                getStoneCountY(ido, idd, board.getBoard()) == 1 and (
                (board.whichPlayer(board.getBoard()[idd]) != board.whichPlayer(
            board.getBoard()[ido]) and (board.getBoard()[idd] != config.__BLANK__))))


def canMoveCHE(ido, idd, board):
    return (int(ido / 9) == int(idd / 9) and 0 == getStoneCountX(ido, idd, board.getBoard())) or (
            (0 == (abs(ido - idd) % 9)) and 0 == (getStoneCountY(ido, idd, board.getBoard())))


def canMoveSHI(ido, idd, board):
    typeStone = board.whichPlayer(board.getBoard()[ido]).lower()

    return idd - ido in config.__LEGAL_士_MOVE_SET__ and (('red' in typeStone and idd in config.__LEGAL_红将_POS__) or (
            'black' in typeStone and idd in config.__LEGAL_黑将_POS__))


def canMoveJIANG(ido, idd, board):
    typeStone = board.whichPlayer(board.getBoard()[ido]).lower()

    return (idd - ido) in config.__PIN_马__ and (('red' in typeStone and idd in config.__LEGAL_红将_POS__) or (
            'black' in typeStone and idd in config.__LEGAL_黑将_POS__))

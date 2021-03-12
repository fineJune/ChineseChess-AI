# -*-coding:utf-8-*-

"""
@author cc
@date 2021/2/17
@intro 类中封装了一系列函数关于界面有关的方法

"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import func
import config




class UI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)

        self.roundGame=0
        self.board = func.Board()
        self.uiInit()

    def uiInit(self):
        self.resize(config.__WINDOWS_HEIGHT__, config.__WINDOWS_WIDTH__)
        self.setMaximumSize(config.__WINDOWS_HEIGHT__, config.__WINDOWS_WIDTH__)
        self.setMinimumSize(config.__WINDOWS_HEIGHT__, config.__WINDOWS_WIDTH__)
        self.setWindowTitle(config.__WINDOWS_NAME__)

    def drawBoard(self):
        self.painer.setPen(Qt.black)
        """画竖线"""
        for i in range(config.__MARGIN_LENGTH__, config.__COUNT_LINE_VERTICAL__ * config.__LINE_SPLIT_LENGTH__,
                       config.__LINE_SPLIT_LENGTH__):
            xb, xe = (i, config.__MARGIN_LENGTH__), (i, config.__MARGIN_LENGTH__ + config.__LENGTH_HORIZON__)

            if i == 1 * config.__MARGIN_LENGTH__ or i == (
                    config.__COUNT_LINE_VERTICAL__ - 2) * config.__LINE_SPLIT_LENGTH__ + config.__MARGIN_LENGTH__:
                self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])
            else:
                xb, xe = (i, config.__MARGIN_LENGTH__), (i, config.__LINE_SPLIT_LENGTH__ * 4 + config.__MARGIN_LENGTH__)
                self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])

                xb, xe = (i, config.__LINE_SPLIT_LENGTH__ * 5 + config.__MARGIN_LENGTH__), (
                    i, config.__MARGIN_LENGTH__ + config.__LENGTH_HORIZON__)
                self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])
            # print(i)

        """画横线"""
        for i in range(config.__MARGIN_LENGTH__, config.__COUNT_LINE_HORIZON__ * config.__LINE_SPLIT_LENGTH__,
                       config.__LINE_SPLIT_LENGTH__):
            xb, xe = (config.__MARGIN_LENGTH__, i), (config.__MARGIN_LENGTH__ + config.__LENGTH_VERTICAL__, i)
            self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])

        """画九宫格"""

        # 上方
        xb, xe = (config.__LINE_SPLIT_LENGTH__ * 5 + config.__MARGIN_LENGTH__, config.__MARGIN_LENGTH__), (
            config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 3,
            config.__LINE_SPLIT_LENGTH__ * 2 + config.__MARGIN_LENGTH__)
        self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])
        xb, xe = (config.__LINE_SPLIT_LENGTH__ * 3 + config.__MARGIN_LENGTH__, config.__MARGIN_LENGTH__), (
            config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 5,
            config.__LINE_SPLIT_LENGTH__ * 2 + config.__MARGIN_LENGTH__)
        self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])

        # 下方
        xb, xe = (config.__LINE_SPLIT_LENGTH__ * 5 + config.__MARGIN_LENGTH__,
                  config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 7), (
                     config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 3,
                     config.__LINE_SPLIT_LENGTH__ * 9 + config.__MARGIN_LENGTH__)
        self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])
        xb, xe = (config.__LINE_SPLIT_LENGTH__ * 5 + config.__MARGIN_LENGTH__,
                  config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 9), (
                     config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 3,
                     config.__LINE_SPLIT_LENGTH__ * 7 + config.__MARGIN_LENGTH__)
        self.painer.drawLine(xb[0], xb[1], xe[0], xe[1])

        # 画字
        self.painer.setFont(QFont("楷体", config.__楚汉河界_字体大小__))
        self.painer.drawText(config.__MARGIN_LENGTH__,
                             config.__MARGIN_LENGTH__ + config.__LINE_SPLIT_LENGTH__ * 4 + config.__MARGIN_LENGTH__ / 2,
                             "\t楚\t汉\t\t\t河\t界")

    def drawStone(self, pos, text, checked=False):
        self.painer.setFont(QFont("华文行楷", config.__象棋大小__))
        # print(pos[1], pos[0])
        self.painer.drawText(pos[0], pos[1], text)

        self.painer.setPen(Qt.black)
        if checked:
            colorCheked = QColor()
            colorCheked.setRgb(*config.__CHECKED_COLOR__)
            colorCheked.setAlphaF(config.__CHECKED_ALPHA__)
            self.painer.setBrush(colorCheked)

        else:
            self.painer.setBrush(Qt.transparent)

        self.painer.drawEllipse(pos[0] - 15, pos[1] - 55, config.__RADIUS__, config.__RADIUS__)

    def stoneInit(self):
        board = self.board.getBoard()
        for i in range(len(board)):
            stone = board[i]
            self.painer.setPen(Qt.black)
            if config.r_将 >= stone >= config.r_兵:
                self.painer.setPen(Qt.red)

            checked = False
            if self.board.checkedStoneID == i:
                checked = True

            if stone != config.__BLANK__:
                self.drawStone(self.posID2PosXY(i), self.board.getStoneFromID(i), checked=checked)

    def posID2PosXY(self, id):
        return (
            (id % (config.__COUNT_LINE_VERTICAL__ - 1) * config.__LINE_SPLIT_LENGTH__) + config.__MARGIN_LENGTH__ - 20,
            int(id / (
                    config.__COUNT_LINE_VERTICAL__ - 1)) * config.__LINE_SPLIT_LENGTH__ + config.__MARGIN_LENGTH__ + 20)

    """下面是一系列事件"""

    def paintEvent(self, a0: QPaintEvent):
        QPainter(self).drawPixmap(self.rect(), QPixmap(config.__IMAGE_BACKGROUND__))
        QPainter(self).fillRect(self.rect(), QColor(255, 255, 255, 50))

        self.rePaint()

        self.drawTips()

    def rePaint(self):
        try:
            del self.painer
        except:
            pass

        self.painer = QPainter(self)
        self.drawBoard()
        self.stoneInit()

    def reDrawBoard(self):
        self.drawBoard()
        self.stoneInit()


    

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        x, y = a0.x(), a0.y()

        idy, idx = round((x - config.__MARGIN_LENGTH__) / config.__LINE_SPLIT_LENGTH__), round(
            (y - config.__MARGIN_LENGTH__) / config.__LINE_SPLIT_LENGTH__)

        id = idx * (config.__COUNT_LINE_VERTICAL__ - 1) + idy



        if self.board.getBoard()[id] != config.__BLANK__ and (self.board.whichPlayer(self.board.getBoard()[
                                                                                         id]) != self.board.currentPlayer and self.board.checkedStoneID == config.__UNCKECKED__):
            print("不合法")
            return

        if self.board.checkedStoneID == config.__UNCKECKED__:
            if self.board.getBoard()[id] != config.__BLANK__:
                self.board.setChecked(id)

        elif self.board.whichPlayer(self.board.getBoard()[id]) != self.board.whichPlayer(
                self.board.getBoard()[self.board.checkedStoneID]):
            print("移动")
            if self.board.canMove(id):
                self.board.move(self.board.checkedStoneID, id)
            else:
                print('不合法')

        elif self.board.whichPlayer(self.board.getBoard()[id]) == self.board.whichPlayer(
                self.board.getBoard()[self.board.checkedStoneID]):
            print("换子")
            self.board.setChecked(id)


        self.update()
    def computerMove(self):
        print('计算机走')
        ai.searchForTime(self.board)
        print(self.board.bestMove)
        self.board.move(*self.board.getMove(self.board.bestMove))

    def drawTips(self):
        self.painer.setFont(QFont("华文行楷", config.__象棋大小__))
        # print(pos[1], pos[0])
        self.painer.drawText(config.__POS_X__, config.__POS_Y__, config.__TIPS__)

        if 'red' in self.board.currentPlayer.lower():
            self.painer.setPen(Qt.red)
        else:
            self.painer.setPen(Qt.black)

        self.painer.drawText(config.__POS_X__, config.__POS_Y__ + 200,
                             '\t红方下子' if 'red' in self.board.currentPlayer.lower() else '\t黑方下子')

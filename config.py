# -*-coding:utf-8-*-

"""
@author cc
@date 2021/2/17
"""

"""窗口属性"""
__WINDOWS_HEIGHT__ = 1200
__WINDOWS_WIDTH__ = 900
__WINDOWS_NAME__ = "智能象棋"
__楚汉河界_字体大小__ = 30
__象棋大小__ = 35

__RADIUS__ = 75
__LINE_SPLIT_LENGTH__ = 80

__COUNT_LINE_HORIZON__ = 11
__COUNT_LINE_VERTICAL__ = 10

__MARGIN_LENGTH__ = 100

__LENGTH_HORIZON__ = __LINE_SPLIT_LENGTH__ * (__COUNT_LINE_HORIZON__ - 2)
__LENGTH_VERTICAL__ = __LINE_SPLIT_LENGTH__ * (__COUNT_LINE_VERTICAL__ - 2)

"""置换表大小"""
__TABLE_SIZE__ = 65535

__TABLE_FILE_NAME__ = "开局表.book"  # 开局表文件名字

"""合法走法"""

__LEGAL_马_MOVE_SET__ = [-19, -17, -11, 7, -7, 11, 17, 19]
__LEGAL_相_MOVE_SET__ = [-20, -16, 16, 20]

__PIN_马__ = [-9, -1, 1, 9]
__PIN_相__ = [-10, -8, 8, 10]
__LEGAL_士_MOVE_SET__ = [-10, -8, 8, 10]
__LEGAL_红兵_过河_MOVE_SET__ = [1, -1, -9]
__LEGAL_黑兵_过河_MOVE_SET__ = [1, -1, 9]
__LEGAL_红兵_MOVE_SET__ = [-9]
__LEGAL_黑兵_MOVE_SET__ = [9]

__LEGAL_红将_POS__ = [66, 67, 68, 75, 76, 77, 84, 85, 86]
__LEGAL_黑将_POS__ = [3, 4, 5, 12, 13, 14, 21, 22, 23]

r_兵 = 0
r_炮 = 1
r_车 = 3
r_马 = 4
r_相 = 5
r_士 = 6
r_将 = 7

b_兵 = 8
b_炮 = 9
b_车 = 10
b_马 = 11
b_相 = 12
b_士 = 13
b_将 = 14

__BLANK__ = -1
__UNCKECKED__ = -2
__BOARD_INIT__ = [
    10, 11, 12, 13, 14, 13, 12, 11, 10,
    -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, 9, -1, -1, -1, -1, -1, 9, -1,
    8, -1, 8, -1, 8, -1, 8, -1, 8,
    -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1,
    0, -1, 0, -1, 0, -1, 0, -1, 0,
    -1, 1, -1, -1, -1, -1, -1, 1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1,
    3, 4, 5, 6, 7, 6, 5, 4, 3, ]

__CHECKED_COLOR__ = (255, 255, 255)
__CHECKED_ALPHA__ = 0.5

__COLOR_BACKGROUND__ = "#681752"

__IMAGE_BACKGROUND__ = ".\\src\\bg.jpg"

__TIPS__ = '\t欢迎挑战'
__POS_X__ = 800
__POS_Y__ = 200

"""子力"""
__VALUE_RED_BING__ = [3, 3, 3, 3, 3, 3, 3, 3, 3,
                      3, 3, 3, 3, 3, 3, 3, 3, 3,
                      3, 3, 3, 3, 3, 3, 3, 3, 3,
                      3, 3, 3, 3, 3, 3, 3, 3, 3,
                      3, 3, 3, 3, 3, 3, 3, 3, 3,
                      1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 1, 1, 1, 1, 1, 1, 1, ]

__VALUE_CHE__ = 8
__VALUE_MA__ = 5
__VALUE_PAO__ = 5
__VALUE_XIANG__ = 3
__VALUE_SHI__ = 3
__VALUE_JIANG__ = 10000

__DEPTH_SEARCH__ = 2

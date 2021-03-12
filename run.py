# -*-coding:utf-8-*-

"""
@author cc
@date 2021/2/17
"""

import ui
from PyQt5.QtWidgets import QApplication
import sys


app=QApplication(sys.argv)

windows=ui.UI()
windows.show()

sys.exit(app.exec_())


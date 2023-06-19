import time

import pyautogui
from pyautogui import position
from pyautogui import moveTo
from pyautogui import click
from pyautogui import typewrite


width,height = pyautogui.size()
print(width,height)


# x,y = position()
# print(x,y)
# 623 384
# 601 422
# moveTo(623,384)
# click(623,384)
# typewrite('111111')
# click(601,422,button='left')

# x,y = position()
# print(x,y)
# 483 252
# 593 387
# 选择印章
# click(483,252,button='left')
# time.sleep(1)
# click(620,506,button='left')
# 输入密码
# click(623,384)
# typewrite('111111')
# click(601,422,button='left')
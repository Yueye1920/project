def div():
    2 / 0
try:
    div()
except ZeroDivisionError as e:
    print('失败')
    raise

# -*- coding: utf-8 -*-

import urllib.request
import re

try:
    sudoku = urllib.request.urlopen(
        'http://cn.sudokupuzzle.org/online2.php?nd=2')
    # print 'http header:/n', sudoku.info()
    # print 'http status:', sudoku.getcode()
    print('url: ' + sudoku.geturl())
    for line in sudoku:  # 就像在操作本地文件
        # print(line)
        matchObj = re.search(r'tmda=\'(\d+)\'', str(line))
        if matchObj:
            # print(matchObj.group(1))
            print(list(map(lambda x: int(x), list(matchObj.group(1))[:81])))
            print(list(map(lambda x: int(x), list(matchObj.group(1))[81:162])))
            break
except Exception as e:
    print(e)
finally:
    if sudoku:
        sudoku.close()

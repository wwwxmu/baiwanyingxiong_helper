# -*- coding: utf-8 -*-

import wda
from PIL import Image
from common import  ocr, methods
from multiprocessing import Pool
import time

c = wda.Client()


while True:
    # 截图
    c.screenshot('screenshot.png')

    img = Image.open("./screenshot.png")

    # 文字识别
    question, choices = ocr.ocr_img(img)
    print('Question: ' + question+'\n')

    p = Pool()
    for i in [1,2,0]:   
        p.apply_async(methods.run_algorithm, args=(i,question, choices))
    p.close()
    p.join()
    go = raw_input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print('------------------------')
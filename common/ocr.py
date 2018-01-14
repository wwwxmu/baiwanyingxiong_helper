# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import multiprocessing as mp
import pytesseract
# tesseract 路径
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/3.05.01/bin/tesseract'
global CONFIG
# 语言包目录和参数
CONFIG = '--tessdata-dir "/usr/local/Cellar/tesseract/3.05.01/share/tessdata/" -psm 6'



def get_word(im):
    word = pytesseract.image_to_string(im, lang='chi_sim', config=CONFIG)
    word = word.replace("_", u"一").replace(u'唧',u"哪")
    return word

def ocr_img(image):

    # 切割题目和选项位置，左上角坐标和右下角坐标,自行测试分辨率
    question_im = image.crop((40, 180, 610, 410)) # iPhone se
    choices_im = image.crop((40, 410, 550, 710)) # iPhone se

    pool = mp.Pool() 
    res = pool.map(get_word, [question_im, choices_im])
    question = res[0].replace("\n", "").replace(u'′',"")[2:]
    question = question.replace(".","")
    choices = res[1].strip().split("\n")
    choices = [ x for x in choices if x != '' ]

    return question, choices


if __name__ == '__main__':
    image = Image.open("../screenshot.png")
    question,choices = ocr_img(image)

    print "识别结果:"
    print question.encode('utf-8')
    for c in choices:
        print c.encode('utf-8')
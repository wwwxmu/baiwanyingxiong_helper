# coding=utf-8

import requests
import webbrowser
from colorama import init,Fore
init()

def open_webbrowser(question,choices):
    # 使用chrome浏览器
    # chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    # webbrowser.get(chrome_path).open(sougou)
    
    # baidu = "https://www.baidu.com/s?ie=UTF-8&wd=%s" % question
    # sougou = "http://www.sogou.com/sogou?query=%s" %question.encode('utf-8')
    web = webbrowser.get('safari').open("https://www.baidu.com/s?ie=UTF-8&wd=%s" %question.encode('utf-8')+" ".join([c.encode('utf-8') for c in choices]))



def count_base_baidu(question,choices):
    # 百度：题目搜索结果包含选项词频计数法
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    counts = []
    if u'不' in question or u'未' in question:
        print('**请注意此题为否定题,选计数最少的**')
    for i in range(len(choices)):
        counts.append(content.encode('utf-8').count(choices[i].encode('utf-8')))
    print "百度统计："
    output(choices, counts)

def count_base_sougou(question,choices):
    # 搜狗：题目搜索结果包含选项词频计数法
    req = requests.get(url='http://www.sogou.com/sogou', params={'query':question})
    content = req.text
    counts = []
    if u'不' in question or u'未' in question:
        print('**请注意此题为否定题,选计数最少的**')
    for i in range(len(choices)):
        counts.append(content.encode('utf-8').count(choices[i].encode('utf-8')))
    print "sougou统计："
    output(choices, counts)

def open_webbrowser_count(question,choices):
    # 题目+选项搜索结果计数法(效果较差)
    if u'不' in question or u'未' in question:
        print('**请注意此题为否定题,选计数最少的**')

    counts = []
    for i in range(len(choices)):
        req = requests.get(url='http://www.baidu.com/s', params={'wd': question + choices[i]})
        content = req.text
        index = content.find(u'百度为您找到相关结果约')+11

        content = content[index:]
        index = content.find(u'个')
        count = content[:index].replace(',', '')
        counts.append(count)
    output(choices, counts)

def output(choices, counts):
    counts = list(map(int, counts))

    # 计数最高
    index_max = counts.index(max(counts))

    # 计数最少
    index_min = counts.index(min(counts))

    if index_max == index_min:
        print(Fore.RED + "高低计数相等此方法失效！" + Fore.RESET)
        return

    for i in range(len(choices)):
        if i == index_max:
            # 绿色为计数最高的答案
            print(Fore.GREEN + "{0} : {1} ".format(choices[i].encode('utf-8'), counts[i]) + Fore.RESET)
        elif i == index_min:
            # 红色为计数最低的答案
            print(Fore.MAGENTA + "{0} : {1}".format(choices[i].encode('utf-8'), counts[i]) + Fore.RESET)
        else:
            print("{0} : {1}".format(choices[i].encode('utf-8'), counts[i]))
    print "======================================\n"


def run_algorithm(al_num, question, choices):
    if al_num == 0:
        open_webbrowser(question,choices)
    elif al_num == 1:
        count_base_sougou(question, choices)
    elif al_num == 2:
        count_base_baidu(question, choices)
    elif al_num == 3:
        open_webbrowser_count(question, choices)

if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    run_algorithm(0, question, choices)
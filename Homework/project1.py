# coding=utf-8
#import sys
from xpinyin import Pinyin
import logging
import rich.progress
import argparse #参数解析
import  os

#工作环境变当前目录
current_path = os.path.dirname(__file__)


os.chdir(current_path)
parse=argparse.ArgumentParser()
parse.add_argument("--str_cities",type=str,default='str_cities',help="Log storage path")
args = parse.parse_args() 

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logger.log', level=logging.INFO,format=LOG_FORMAT)
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')

listcity=[]#从文件读取城市

#Process 对象传入的参数就是进度条会显示的内容
with rich.progress.open("chinaCity.csv", "r") as file:#进度条
    for line in file:
        rs = line.rstrip('市\n')#读取文件去掉'\n'和“市”
        listcity.append(rs)

    
pin = Pinyin()# 实例化对象
str_cities = input("请输出您想查询的城市，多个城市之间用空格分隔：")
 

inputcity = str_cities.split(" ")#根据空格切
str="查询："+str_cities
inputcity=list(filter(None,inputcity))#去掉多的空格 返回迭代对象强制转回列表
logging.info(str)#写日志

#查询函数 查询结果唯一并输出首字母 如果模糊匹配上了则输出可能的城市名称但不输出字母
def Find(findcity,listcity):
    print("您查询的是：",findcity)
    outputcity=""#最后要输出的城市首字母
    maycity=[]#模糊匹配系统提示
    for chinacity in listcity :
        if chinacity == findcity:
                outputcity=chinacity
                break
        elif chinacity.find(findcity)!=-1 :
                    maycity.append(chinacity)
    if outputcity :
            print(outputcity,":",end=" ")
            for i in range(len(outputcity)):
                print(pin.get_pinyin(outputcity[i], " ")[0].upper(),end="")
            print("\n")
    else :
        print("查询失败!")
        if maycity :
            print("您可能想查询：")
            for may in maycity:
                print(may)
        print("")

for findcity in inputcity:#依次查询
    Find(findcity,listcity)

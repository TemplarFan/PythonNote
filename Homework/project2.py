#coding = utf-8
import requests
from bs4 import BeautifulSoup
import re
import xlrd
import xlwt
import  os
from xpinyin import Pinyin
import logging
import rich.progress
import time
import tkinter
import tkinter.ttk
from tkinter.messagebox import *
import tkinter.font as tkFont




#工作环境变当前目录
current_path = os.path.dirname(__file__)
os.chdir(current_path)

houselist = []#全局变量 存放爬取到的所有二手房信息

#传入爬取到的所有二手房信息，存储的文件名，查询的城市 将数据保存到excel中 
def saveData(houselist, savepath,city): 
    print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet(city, cell_overwrite_ok=True)  # 创建页签 为城市名
    col = ('小区','商圈','户型','面积(平米)','朝向','装修','楼层','年代','结构','总价(万)','单价','标题')
    for i in range(len(col)):
            sheet.write(0, i, col[i])  #第一行各列标题        
    for i in range(len(houselist)):
        house = houselist[i]
        for j in range(len(house)):
            sheet.write(i + 1, j, house[j])  # 按行写入每间房数据
    book.save(savepath)


#爬取二手房信息
#从文本框获取输入的城市，变成拼音首字母
def Search_City(): 
    listcity = []  # 从文件读取城市
    # Process 对象传入的参数就是进度条会显示的内容
    with rich.progress.open("captain.csv", "r") as file:  # 进度条
        for line in file:
            rs = line.rstrip('\n')  # 读取文件去掉'\n'
            listcity.append(rs)

    pin = Pinyin()  # 实例化对象
    inputcity = text.get().rstrip().rstrip('\n')#去掉换行符 从文本框获取输入的城市
    if(inputcity==""):#如果未输入信息
        showerror("错误","请输入要查询的城市")
        return

    str = "查询："+inputcity
    logging.info(str)  # 写日志

    outputcity = "" #查询的城市 
    cityname = ""# 最后要输出的城市首字母
    maycity = []  # 模糊匹配系统提示
    for chinacity in listcity:
        if chinacity == inputcity:
            outputcity = chinacity
            break
        elif chinacity.find(inputcity) != -1:
            maycity.append(chinacity)
    if outputcity:
        for i in range(len(outputcity)):
            if (outputcity == '重庆'):#多音字bug
                cityname = 'cq'
                break
            else:
                cityname += pin.get_pinyin(outputcity[i], " ")[0].lower()
            #查询成功调用爬虫
        houselist = [] #存放所有二手房信息
        houselist = SecondHouse_Info(cityindex=cityname,cityname=outputcity)#返回所有信息

    else:
        title = "查询失败!"
        if maycity:
            str = "您可能想查询:\n"
            str += " , ".join(maycity)  
        else:
            str = "请重新输入"
        showinfo(title,str)
    return houselist #返回爬取到的所有信息

# 链家的二手房基础页面只显示最多100页，每页30个房源的数据
def SecondHouse_Info(cityindex,cityname):#拼音首字母  城市名
    houselist = []#所有房子信息 元素为每一间房子的信息
    page = 3 # 用于定义页数 
    for i in range(1,page):
        housepage = []#存放每一页所有二手房的信息
        time.sleep(1)
        url = 'https://{}.lianjia.com/ershoufang/pg'.format(cityindex)+str(i)
        #用户代理
        headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

        }
        try:#有些城市没有链家
            request = requests.get(url,headers = headers)
        except:
            showerror("错误","暂无该城市信息")
            btnsave.config(state='disable')
            return
        request.encoding='utf-8'
        html = request.text
        soup = BeautifulSoup(html,'html.parser')#解析 提取标签
        infos = soup.find('ul',{'class':'sellListContent'}).find_all('li')#通过属性进行查找
            #所有信息都在<ul class="sellListContent" log-mod="list">
            #<li class="clear LOGVIEWDATA LOGCLICKDATA">下面
        for info in infos:
            title = info.find('div',{'class':'title'}).find('a').get_text()# 获取房源标题 在title下的a标签
            #get_text()：获取到tag中包含的所有文版内容包括子孙tag中的内容,字符串返回
            # 由于小区名字和小区所属商圈都在class=positionInfo这个切片下面，所以需要先将两个名字放入列表，然后分别提取
            location = info.find('div',{'class':'positionInfo'}).find_all('a')
            data_list = [l.text for l in location]
            housing = data_list[0]#小区
            business = data_list[1]#商圈
            

            # 房子的具体信息，需要先转为列表然后切片
            houseinfo = info.find('div',{'class':'houseInfo'}).get_text()
            houseinfolist = houseinfo.split('|')#放在一起用|分开

            roominfo = houseinfolist[0]#户型
            # area = re.findall(r'-?\d+\.?\d*e?-?\d*?',houseinfolist[1])[0]#面积
            area = houseinfolist[1]
            orientation = houseinfolist[2]#朝向
            fitment = houseinfolist[3]#装修
            level = houseinfolist[4]#楼层

            #有的不一定有楼龄 但楼龄一定数字开头 用正则表达式匹配
            pattern = re.compile('[0-9]+')
            match = pattern.findall(houseinfolist[5])
            if match:
                year = houseinfolist[5]#楼龄
                structure = houseinfolist[6]#结构
            else:
                year = "暂无信息" 
                structure = houseinfolist[5]

            totalprice = info.find('div',{'class':'totalPrice'}).find('span').text #总价

            # unitprice = re.sub('\D','',info.find('div', {'class': 'unitPrice'}).find('span').text)
            unitprice = info.find('div',{'class':'unitPrice'}).find('span').text #每平单价

            houselist.append([housing,business,roominfo,area,orientation,fitment,level,year,structure,totalprice,unitprice,title])
            housepage.append([housing,business,roominfo,area,orientation,fitment,level,year,structure,totalprice,unitprice,title])
            #('小区','商圈','户型','面积','朝向','装修','楼层','年代','结构','总价(万)','单价','标题')
            #显示数据
        for house in housepage: 
            housetree.insert('','end',values=house) # 添加数据到末尾
            #在表格结构中，要显示的数值。这些数值是按照逻辑结构赋值的，也就是按照columns设定的列次序来赋值。
            # 如果输入的个数少于columns指定列数，则插入空白字符串
            housetree.update()#及时更新

    btnsave.config(state='active')#激活保存按钮
    showinfo("成功","查询完成！")
    return houselist


def ShowInfo():
    childlist = housetree.get_children()#获取所有对象 返回root子节点
    for child in childlist:
        housetree.delete(child)#删除指定的item,子节点也会被一起删除，但是第一层节点不会被删除
    global houselist    
    houselist = Search_City()


    




def SaveInfo():
    global houselist
    cityname = text.get().rstrip().rstrip('\n')
    saveData(houselist,cityname+"二手房信息.xls",cityname)
    showinfo("提示", "保存成功")
    btnsave.config(state='disable')#只能保存一次

#GUI

root = tkinter.Tk()#主窗口
root.title("二手房信息")
root.geometry('1400x700')
root.resizable(width=False,height=False)

fontStyle = tkFont.Font(family="楷体", size=18)#字体风格
fontStyle2 = tkFont.Font(family="微软雅黑", size=15)

text =tkinter.Entry(root,font=("微软雅黑", 12))#文本框
text.grid(in_=root,row=0,column=1,sticky='we')#所在行列 左右延申

label = tkinter.Label(root,text="请输入城市名称",font=fontStyle)#标签
label.grid(in_=root,row=0,column=0,sticky="e")



btnsearch = tkinter.Button(root,text="查询",command=ShowInfo,font=("微软雅黑", 10),height=1)#查询按钮
btnsearch.grid(row=0,column=2,sticky='w')

btnsave = tkinter.Button(root,text="保存数据",command=SaveInfo,font=fontStyle)#保存数据按钮
btnsave.grid(row=2,column=2,sticky='ne')
btnsave.config(state='disable')#只有查询成功后才能保存


columns = ['小区','商圈','户型','面积','朝向','装修','楼层','年代','结构','总价(万)','单价','标题']
housetree = tkinter.ttk.Treeview(master=root,columns=columns,height=20,show='headings')#隐藏表头
style = tkinter.ttk.Style()
style.configure("Treeview.Heading", font=("微软雅黑", 12))#设置标题
style.configure("Treeview", font=("微软雅黑", 12))#设置输出内容的字体

#设置或者查询表头行的配置参数。如果是表格形式的，column是列的位置(就是第几列，从0计数）或者列的别名
housetree.heading('小区', text='小区',)  # 定义表头
housetree.heading('商圈', text='商圈', )
housetree.heading('户型', text='户型', ) 
housetree.heading('面积', text='面积', )  
housetree.heading('朝向', text='朝向', )  
housetree.heading('装修', text='装修', )  
housetree.heading('楼层', text='楼层', ) 
housetree.heading('年代', text='年代', )  
housetree.heading('结构', text='结构', )  
housetree.heading('总价(万)', text='总价(万)', )  
housetree.heading('单价', text='单价', )  
housetree.heading('标题', text='标题', )  

housetree.column('小区', width=105, minwidth=50,anchor='s',)#anchor对齐模式
housetree.column('商圈', width=70, minwidth=50, anchor='s',stretch=True)#修改指定列的配置
housetree.column('户型', width=75, minwidth=50, anchor='s',)
housetree.column('面积', width=85, minwidth=50, anchor='s',)
housetree.column('朝向', width=50, minwidth=50, anchor='s',)
housetree.column('装修', width=50, minwidth=50, anchor='s',)
housetree.column('楼层', width=85, minwidth=50, anchor='s',)
housetree.column('年代', width=75, minwidth=50, anchor='s',)
housetree.column('结构', width=70, minwidth=50, anchor='s',)
housetree.column('总价(万)', width=55, minwidth=50, anchor='s',)
housetree.column('单价', width=85, minwidth=50, anchor='s',)
housetree.column('标题', width=270, minwidth=50, anchor='s',stretch=True)
housetree.grid(in_=root,row=1,columnspan=3,padx=10,pady=10,ipadx=150,ipady=80,sticky="nesw")


root.mainloop()


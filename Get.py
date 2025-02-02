# 导入数据请求模块 安装命令：pip install requests
import requests
# 正则表达式 不需要安装
import re
# 导入json 不需要安装
import json
# 导入进程模块
import subprocess  
# os模块是Python中整理文件和目录最为常用的模块
import os

import ffmpeg

# 要请求的网址：B站视频网址
# 这个变量需要替换成你要下载的视频网址
url = "https://www.bilibili.com/video/BV1Ka4y1i7Wt/?spm_id_from=333.1007.top_right_bar_window_custom_collection.content.click&vd_source=35037e7e4f3f7797707c66ee308b37de"

# 添加headers请求头，对Python解释器进行伪装
# referer 和 User-Agent要改写成字典形式
headers = {
    "referer":"https://www.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

# 用 requests 的 get 方法访问网页
response = requests.get(url=url, headers=headers)

# 返回响应状态码：<Response [200]>
print("返回200，则网页请求成功：",response)

# .text获取网页源代码
# 提取视频标题
# 调用 re 的 findall 方法，去response.text中匹配我们要的标题
# 正则表达式提取的数据返回的是一个列表，用[0]从列表中取值
title = re.findall('<h1 title="(.*?)"', response.text)[0]
# 如果标题里有[\/:*?<>|]特殊字符，直接删除
title = re.sub(r"[\/:*?<>|]","",title)
print("视频标题为：",title)


# 提取 playinfo 里的数据
# 调用 re的 findall 方法，去 response.text 中匹配我们要的数据
# 正则表达式提取的数据返回的是一个列表，用[0]从列表中取值
html_data =  re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]

# html_data是字符串类型，将字符串转换成字典
json_data=json.loads(html_data)


# 提取视频画面网址
video_url = json_data["data"]["dash"]["video"][0]["baseUrl"]
print("视频画面地址为：", video_url)
# 提取音频网址
audio_url = json_data["data"]["dash"]["audio"][0]["baseUrl"]
print("音频地址为：", audio_url)

# response.content获取响应体的二进制数据
video_content = requests.get(url=video_url,headers=headers).content
audio_content = requests.get(url=audio_url,headers=headers).content

# 创建mp4文件，写入二进制数据
with open (title+".mp4", mode = "wb") as f :
    f.write(video_content)
# 创建mp3文件，写入二进制数据
with open (title+".mp3", mode = "wb") as f :
    f.write(audio_content)

print("数据写入成功！")

# 合成视频
# ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
cmd =f"ffmpeg -i {title}.mp4 -i {title}.mp3 -c:v copy -c:a aac -strict experimental {title}(最终版).mp4"
subprocess.run(cmd,shell=True)
print( '视频合成成功！') 

# 删除不需要的mp3和mp4文件
os.remove(f'{title}.mp3')
os.remove(f'{title}.mp4')

print("程序结束！")
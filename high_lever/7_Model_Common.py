import pdfplumber
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image  # pillow
# import pygame  # 游戏GUI
import jieba
# Pyinstaller 用于将Python源代码进行打包，生成可执行文件的模块
# 打包语法：pyinstaller -F 源文件


# pdfplumber 处理pdf
with pdfplumber.open('FrontEndDeveloper.pdf') as pdf:
    for i in pdf.pages:
        # print(i, type(i))
        print(i.extract_text())
        print()
        print('+++++++++++++++++++++++++++++++++++')

# numpy 处理数组
n1 = plt.imread('20190316115819.jpg')
print(type(n1), n1)
plt.imshow(n1)
n2 = np.array([0.299, 0.587, 0.114])
x = np.dot(n1, n2)
plt.imshow(x, cmap='gray')
plt.show()

print('++++++++++++++++++++++++++')
# pandas 处理excel
df = pd.read_excel('phone.xlsx')
# print(df)
# 解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置画布大小
plt.figure(figsize=(10, 6))
labels = df['name']
y = df['beijing']
# 绘制饼图
plt.pie(y, labels=labels, autopct='%1.1f%%')
# 设置x，y轴刻度一致
plt.axis('equal')
plt.title('phone sales')
plt.show()

# matplotlib 处理数据可视化, 图形处理
# plt.show()


# 处理图像颜色，滤镜。。。
im = Image.open('20190316115819.jpg')
# print(type(im), im)
r, g, b = im.split()
# print(r, g, b)
# 合并通道， 其中mode表示色彩， bands表示的是新的色彩通道
om = Image.merge(mode='RGB', bands=(g, r, b))
om.save('new_2019.jpg')

# GUI 图形用户界面


# jieba 中文分词
# lst = jieba.lcut(s)
# set1 = set(lst)
# d = {}
# for item in set1:
#     d[item] = 0
#
# for item in lst:
#     if item in d:
#         d[item] = d[item] + 1
#
# # 将字典转成列表排序
# new_lst = []
# for item in d:
#     new_lst.append([item, d[item]])
# new_lst.sort(key=lambda val: val[1], reverse=True)

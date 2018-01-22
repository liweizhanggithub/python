# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import seaborn as sns
from pylab import mpl

font = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                      size=20)
font1 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=18.5)
font0 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=17.5)
font2 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=22)
font3 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=13)


# """
# 北京-上海
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\高铁\\聚类结果\\北京-上海1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'旅行时间', u'停站数', u'定员',u'列车数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的旅行速度"""
# p1 = df1[u'旅行时间'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((100, 280))
# ax1.set_yticklabels(np.arange(100,281,20),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 55))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的旅行速度', fontproperties=font1)
#
#
# """每类产品的定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0,1200))
# ax2.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 53))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的定员', fontproperties=font1)
#
#
# """每列产品的停站数分布"""
# p3 = df1[u'停站数'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,11))
# ax3.set_yticklabels(np.arange(0,11,2),fontproperties=font0)
#
# ax3.set_xlim((-0.9, 53))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的停站数分布', fontproperties=font1)
#
#
# """每类产品的列车数量分布"""
# p4 = df1[u'列车数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((1,13))
# ax4.set_yticklabels(np.arange(1,14,2),fontproperties=font0)
#
# ax4.set_xlim((-0.5,6.5))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类',u'第6类',u'第7类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的列车数量', fontproperties=font1)
#
# plt.show()

# """
# 北京-武汉
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\高铁\\聚类结果\\北京-武汉1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'旅行时间', u'停站数', u'定员',u'列车数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的旅行速度"""
# p1 = df1[u'旅行时间'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((200, 301))
# ax1.set_yticklabels(np.arange(200,301,20),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 36))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的旅行速度', fontproperties=font1)
#
#
# """每类产品的定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0,1200))
# ax2.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 35))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的定员', fontproperties=font1)
#
#
# """每列产品的停站数分布"""
# p3 = df1[u'停站数'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,15))
# ax3.set_yticklabels(np.arange(0,15,2),fontproperties=font0)
#
# ax3.set_xlim((-0.9, 35))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的停站数分布', fontproperties=font1)
#
#
# """每类产品的列车数量分布"""
# p4 = df1[u'列车数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((1,9))
# ax4.set_yticklabels(np.arange(1,9,1),fontproperties=font0)
#
# ax4.set_xlim((-0.5,4.5))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的列车数量', fontproperties=font1)
#
# plt.show()


# """
# 北京-西安
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\高铁\\聚类结果\\北京-西安1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'旅行时间', u'停站数', u'定员',u'列车数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的旅行速度"""
# p1 = df1[u'旅行时间'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((100, 301))
# ax1.set_yticklabels(np.arange(100,301,50),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 21))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的旅行速度', fontproperties=font1)
#
#
# """每类产品的定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0,1200))
# ax2.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 21))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的定员', fontproperties=font1)
#
#
# """每列产品的停站数分布"""
# p3 = df1[u'停站数'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,13))
# ax3.set_yticklabels(np.arange(0,13,2),fontproperties=font0)
#
# ax3.set_xlim((-0.9,21))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的停站数分布', fontproperties=font1)
#
#
# """每类产品的列车数量分布"""
# p4 = df1[u'列车数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((1,6))
# ax4.set_yticklabels(np.arange(1,6,1),fontproperties=font0)
#
# ax4.set_xlim((-0.5,3.98))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的列车数量', fontproperties=font1)
#
# plt.show()


# """
# 北京-南京
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\高铁\\聚类结果\\北京-南京1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'旅行时间', u'停站数', u'定员',u'列车数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的旅行速度"""
# p1 = df1[u'旅行时间'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((50, 301))
#  ax1.set_yticklabels(np.arange(50,301,50),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 69))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的旅行速度', fontproperties=font1)
#
#
# """每类产品的定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0,1200))
# ax2.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 67))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的定员', fontproperties=font1)
#
#
# """每列产品的停站数分布"""
# p3 = df1[u'停站数'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,9))
# ax3.set_yticklabels(np.arange(0,9,1),fontproperties=font0)
#
# ax3.set_xlim((-0.9,69))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的停站数分布', fontproperties=font1)
#
#
# """每类产品的列车数量分布"""
# p4 = df1[u'列车数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((0,17))
# ax4.set_yticklabels(np.arange(0,17,2),fontproperties=font0)
#
# ax4.set_xlim((-0.5,6.3))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类',u'第6类',u'第7类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的列车数量', fontproperties=font1)
#
# plt.show()



# """
# 北京-长沙
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\高铁\\聚类结果\\北京-长沙1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'旅行时间', u'停站数', u'定员',u'列车数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的旅行速度"""
# p1 = df1[u'旅行时间'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((200, 281))
# ax1.set_yticklabels(np.arange(200,281,10),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 25))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的旅行速度', fontproperties=font1)
#
#
# """每类产品的定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0,1200))
# ax2.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 25))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的定员', fontproperties=font1)
#
#
# """每列产品的停站数分布"""
# p3 = df1[u'停站数'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((2,15))
# ax3.set_yticklabels(np.arange(2,15,2),fontproperties=font0)
#
# ax3.set_xlim((-0.9,25))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的停站数分布', fontproperties=font1)
#
#
# """每类产品的列车数量分布"""
# p4 = df1[u'列车数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((0,7))
# ax4.set_yticklabels(np.arange(0,7,1),fontproperties=font0)
#
# ax4.set_xlim((-0.6,4.5))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的列车数量', fontproperties=font1)
#
# plt.show()



#
# """
# 北京-哈尔滨航班
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-哈尔滨-航空1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'出发时间', u'票价', u'定员',u'航班数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的票价"""
# p1 = df1[u'票价'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((300, 749))
# ax1.set_yticklabels(np.arange(300,749,50),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 27))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的票价', fontproperties=font1)
#
#
# """每类产品的航班定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((100,201))
# ax2.set_yticklabels(np.arange(100,201,20),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 26))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的航班定员', fontproperties=font1)
#
#
# """每列产品的出发时间分布"""
# p3 = df1[u'出发时间'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0.2,1.1))
# ax3.set_yticklabels(['4:48','9:36','14:24','19:12','24:00'],fontproperties=font0)
#
# ax3.set_xlim((-0.9,27))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的出发时间分布', fontproperties=font1)
#
#
# """每类产品的航班数量分布"""
# p4 = df1[u'航班数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((0,6))
# ax4.set_yticklabels(np.arange(0,7,1),fontproperties=font0)
#
# ax4.set_xlim((-0.6,4.5))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的航班数量', fontproperties=font1)
#
# plt.show()


# """
# 北京-上海航班
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-上海-航空1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'出发时间', u'票价', u'定员',u'航班数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的票价"""
# p1 = df1[u'票价'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((400, 1200))
# ax1.set_yticklabels(np.arange(400,1201,100),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 63))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的票价', fontproperties=font1)
#
#
# """每类产品的航班定员"""
# p2 = df1[u'定员'].plot(kind='bar',
# ax=ax2,
#     color='darksalmon',
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((100,350))
# ax2.set_yticklabels(np.arange(100,351,50),fontproperties=font0)
#
# ax2.set_xlim((-0.9, 62))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每类产品的航班定员', fontproperties=font1)
#
#
# """每列产品的出发时间分布"""
# p3 = df1[u'出发时间'].plot(kind='bar',
# ax=ax3,
#      color="orchid",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0.2,1))
# ax3.set_yticklabels(['4:48','7:12','9:36','12:00','14:24','16:48','19:12','21:36','24:00'],fontproperties=font0)
#
# ax3.set_xlim((-0.9,63))
# ax3.set_xticklabels([],fontproperties=font0)
#
# ax3.set_title(u'每列产品的出发时间分布', fontproperties=font1)
#
#
# """每类产品的航班数量分布"""
# p4 = df1[u'航班数量'].plot(kind='bar',
# ax=ax4,
#      color="limegreen",
#     alpha=1)
#
# ax4.grid()
# ax4.set_frame_on(False)
# ax4.patch.set_visible(True)
#
# ax4.set_ylim((1,10))
# ax4.set_yticklabels(np.arange(1,10,1),fontproperties=font0)
#
# ax4.set_xlim((-0.6,7.5))
# ax4.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类',u'第6类',u'第7类',u'第8类'],fontproperties=font0,rotation=0)
#
# ax4.set_title(u'每类产品的航班数量', fontproperties=font1)
#
# plt.show()

#
# """
# 北京-武汉航班
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-武汉-航空1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(3, 1, 1)
# ax2 = fig.add_subplot(3, 1, 2)
# ax3 = fig.add_subplot(3, 1, 3)
# # ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'出发时间', u'票价',u'航班数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的票价"""
# p1 = df1[u'票价'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((200, 1800))
# ax1.set_yticklabels(np.arange(200,1801,200),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 27))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的票价', fontproperties=font1)
#
# """每列产品的出发时间分布"""
# p2 = df1[u'出发时间'].plot(kind='bar',
# ax=ax2,
#      color="orchid",
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0.2,1))
# ax2.set_yticklabels(['4:48','7:12','9:36','12:00','14:24','16:48','19:12','21:36','24:00'],fontproperties=font0)
#
# ax2.set_xlim((-0.9,27))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每列产品的出发时间分布', fontproperties=font1)
#
#
# """每类产品的航班数量分布"""
# p3 = df1[u'航班数量'].plot(kind='bar',
# ax=ax3,
#      color="limegreen",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,5))
# ax3.set_yticklabels(np.arange(0,6,1),fontproperties=font0)
#
# ax3.set_xlim((-0.6,5.5))
# ax3.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类',u'第6类'],fontproperties=font0,rotation=0)
#
# ax3.set_title(u'每类产品的航班数量', fontproperties=font1)
#
# plt.show()



# """
# 北京-西安航班
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-西安-航空1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(3, 1, 1)
# ax2 = fig.add_subplot(3, 1, 2)
# ax3 = fig.add_subplot(3, 1, 3)
# # ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'出发时间', u'票价',u'航班数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的票价"""
# p1 = df1[u'票价'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((300, 1100))
# ax1.set_yticklabels(np.arange(300,1101,100),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 33))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的票价', fontproperties=font1)
#
# """每列产品的出发时间分布"""
# p2 = df1[u'出发时间'].plot(kind='bar',
# ax=ax2,
#      color="orchid",
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0.2,1))
# ax2.set_yticklabels(['4:48','7:12','9:36','12:00','14:24','16:48','19:12','21:36','24:00'],fontproperties=font0)
#
# ax2.set_xlim((-0.9,33))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每列产品的出发时间分布', fontproperties=font1)
#
#
# """每类产品的航班数量分布"""
# p3 = df1[u'航班数量'].plot(kind='bar',
# ax=ax3,
#      color="limegreen",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((1,8))
# ax3.set_yticklabels(np.arange(1,9,1),fontproperties=font0)
#
# ax3.set_xlim((-0.6,5.5))
# ax3.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类',u'第5类',u'第6类'],fontproperties=font0,rotation=0)
#
# ax3.set_title(u'每类产品的航班数量', fontproperties=font1)
#
# plt.show()


# """
# 北京-南京航班
# """
# df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-南京-航空1.xlsx',sheetname=0)
#
# """
# 产品特性画图
# """
# # fig = plt.figure(facecolor='white')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# # plt.axes(axisbg='white')
# ax1 = fig.add_subplot(3, 1, 1)
# ax2 = fig.add_subplot(3, 1, 2)
# ax3 = fig.add_subplot(3, 1, 3)
# # ax4 = fig.add_subplot(2, 2, 4)
# df1 = df[[u'出发时间', u'票价',u'航班数量']]
# plt.style.use('ggplot')
# # ax1.grid()
#
# """每类产品的票价"""
# p1 = df1[u'票价'].plot(kind='bar',
# ax=ax1,
#     color='cornflowerblue',
#     alpha=1)
#
# ax1.set_frame_on(False)
# ax1.patch.set_visible(True)
#
# ax1.set_ylim((0, 1400))
# ax1.set_yticklabels(np.arange(0,1401,200),fontproperties=font0)
#
# ax1.set_xlim((-0.9, 19))
# ax1.set_xticklabels([],fontproperties=font0)
#
# ax1.set_title(u'每类产品的票价', fontproperties=font1)
#
# """每列产品的出发时间分布"""
# p2 = df1[u'出发时间'].plot(kind='bar',
# ax=ax2,
#      color="orchid",
#     alpha=1)
#
# ax2.grid()
# ax2.set_frame_on(False)
# ax2.patch.set_visible(True)
#
# ax2.set_ylim((0.3,1))
# ax2.set_yticklabels(['7:12','9:36','12:00','14:24','16:48','19:12','21:36','24:00'],fontproperties=font0)
#
# ax2.set_xlim((-0.9,19))
# ax2.set_xticklabels([],fontproperties=font0)
#
# ax2.set_title(u'每列产品的出发时间分布', fontproperties=font1)
#
#
# """每类产品的航班数量分布"""
# p3 = df1[u'航班数量'].plot(kind='bar',
# ax=ax3,
#      color="limegreen",
#     alpha=1)
#
# ax3.grid()
# ax3.set_frame_on(False)
# ax3.patch.set_visible(True)
#
# ax3.set_ylim((0,6))
# ax3.set_yticklabels(np.arange(0,7,1),fontproperties=font0)
#
# ax3.set_xlim((-0.5,3.9))
# ax3.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类'],fontproperties=font0,rotation=0)
#
# ax3.set_title(u'每类产品的航班数量', fontproperties=font1)
#
# plt.show()

"""
北京-长沙航班
"""
df = pd.read_excel(u'G:\\000bigpaper\\2\\2.3\\航空\\航空聚类结果\\北京-长沙-航空1.xlsx',sheetname=0)

"""
产品特性画图
"""
# fig = plt.figure(facecolor='white')
fig = plt.figure()
plt.subplots_adjust(wspace=0.1)
# plt.axes(axisbg='white')
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)
# ax4 = fig.add_subplot(2, 2, 4)
df1 = df[[u'出发时间', u'票价',u'航班数量']]
plt.style.use('ggplot')
# ax1.grid()

"""每类产品的票价"""
p1 = df1[u'票价'].plot(kind='bar',
ax=ax1,
    color='cornflowerblue',
    alpha=1)

ax1.set_frame_on(False)
ax1.patch.set_visible(True)

ax1.set_ylim((0, 1200))
ax1.set_yticklabels(np.arange(0,1201,200),fontproperties=font0)

ax1.set_xlim((-0.9, 21))
ax1.set_xticklabels([],fontproperties=font0)

ax1.set_title(u'每类产品的票价', fontproperties=font1)

"""每列产品的出发时间分布"""
p2 = df1[u'出发时间'].plot(kind='bar',
ax=ax2,
     color="orchid",
    alpha=1)

ax2.grid()
ax2.set_frame_on(False)
ax2.patch.set_visible(True)

ax2.set_ylim((0,1))
# ax2.set_yticklabels(['0:00','2:24','4:48','7:12','9:36','12:00','14:24','16:48','19:12','21:36','24:00'],fontproperties=font0)
ax2.set_yticklabels(['0:00','4:48','9:36','14:24','19:12','24:00'],fontproperties=font0)

ax2.set_xlim((-0.9,21))
ax2.set_xticklabels([],fontproperties=font0)

ax2.set_title(u'每列产品的出发时间分布', fontproperties=font1)


"""每类产品的航班数量分布"""
p3 = df1[u'航班数量'].plot(kind='bar',
ax=ax3,
     color="limegreen",
    alpha=1)

ax3.grid()
ax3.set_frame_on(False)
ax3.patch.set_visible(True)

ax3.set_ylim((0,6))
ax3.set_yticklabels(np.arange(0,7,1),fontproperties=font0)

ax3.set_xlim((-0.5,3.5))
ax3.set_xticklabels([u'第1类',u'第2类',u'第3类',u'第4类'],fontproperties=font0,rotation=0)

ax3.set_title(u'每类产品的航班数量', fontproperties=font1)

plt.show()

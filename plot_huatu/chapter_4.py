# -*- coding: utf-8 -*-
from __future__ import division
import pandas as pd
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns
from pylab import mpl
from numpy import linspace
from matplotlib import cm

font = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                      size=16)
font1 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=14)
font2 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=18)
font3 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=11)
font4 = FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
                       size=20)
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.style.use('seaborn-white')


"""北京-哈尔滨 各类方法每类产品分担率堆积条形图"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to哈尔_TRAIN_AIR_whole.xlsx',sheetname='Sheet3')
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to哈尔_TRAIN_AIR_whole.xlsx',sheetname='Sheet4')
#
# color1=['greenyellow','gold','yellow','palegreen','orange','turquoise','cornflowerblue','hotpink','salmon','greenyellow','salmon','gold','turquoise','cyan','deepskyblue','orchid','yellowgreen','orange']
#
# a = df.plot(kind='barh', alpha=0.54, stacked=True,color=color1)
#
# # 对应位置上显示数据，思想就是先求累加和，然后位置1的数据添加在位置1的1/2处，
# # 其他的添加到相应位置的累加和 - （相应位置的1/2）,'%.2f%%' % (df.ix[i,j]*100)是设置成百分数形式显示
# for i in range(len(df)):
#     for j in range(len(df.ix[1])):
#         if j == 0:
#             plt.text(df1.ix[i, j] / 2-0.013, i, '%.2f%%' % (df.ix[i, j] * 100),
#                      fontproperties=font, va='center', rotation='horizontal')
#         else:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j]-0.013, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#
# plt.xlim((0.0, 1.0))
# plt.ylim(-0.5,4.5)
#
# plt.legend((u'T1', u'T2', u'T3', u'T4',u'A1',u'A2',u'A3',u'A4',u'A5'),
#            loc='lower center', prop=font2, ncol=1,bbox_to_anchor=(1.043, 0.28))
#
# plt.xticks(np.arange(0.0,
#                      1.1,
#                      0.2),
#            [u'0.00%',
#             u'20.00%',
#             u'40.00%',
#             u'60.00%',
#             u'80.00%',
#             u'100.00%'],
#            fontproperties=font2)
# plt.yticks(np.arange(0,5,1), [u'分阶段估计法', u'同时估计法',
#                                 u'同时与分阶段结合', u'MNL模型',u'实际结果'], fontproperties=font2)
# plt.show()

"""北京-西安 各类方法每类产品分担率堆积条形图"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to西安_TRAIN_AIR_whole.xlsx',sheetname='Sheet3')
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to西安_TRAIN_AIR_whole.xlsx',sheetname='Sheet4')
#
# color1=['greenyellow','gold','yellow','palegreen','orange','turquoise','cornflowerblue','hotpink','salmon','deepskyblue','orchid','yellowgreen']
#
# # a = df.plot(kind='barh', alpha=0.65, stacked=True,color=color1)
# a = df.plot(kind='barh', alpha=0.54, stacked=True,color=color1)
#
# # 对应位置上显示数据，思想就是先求累加和，然后位置1的数据添加在位置1的1/2处，
# # 其他的添加到相应位置的累加和 - （相应位置的1/2）,'%.2f%%' % (df.ix[i,j]*100)是设置成百分数形式显示
# for i in range(len(df)):
#     for j in range(len(df.ix[1])):
#         if j == 0:
#             plt.text(df1.ix[i, j] / 2-0.02, i, '%.2f%%' % (df.ix[i, j] * 100),
#                      fontproperties=font, va='center', rotation='horizontal')
#         else:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j]-0.02, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#
# plt.xlim((0.0, 1.0))
# plt.ylim(-0.5,4.5)
#
# plt.legend((u'T1', u'T2', u'T3', u'T4',u'A1',u'A2',u'A3',u'A4',u'A5',u'A6'),
#            loc='lower center', prop=font2, ncol=1,bbox_to_anchor=(1.043, 0.21))
#
# plt.xticks(np.arange(0.0,
#                      1.1,
#                      0.2),
#            [u'0.00%',
#             u'20.00%',
#             u'40.00%',
#             u'60.00%',
#             u'80.00%',
#             u'100.00%'],
#            fontproperties=font2)
# plt.yticks(np.arange(0,5,1), [u'分阶段估计法', u'同时估计法',
#                                 u'同时与分阶段结合', u'MNL模型',u'实际结果'], fontproperties=font2)
# plt.show()

"""北京-武汉 各类方法每类产品分担率堆积条形图"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to武汉_TRAIN_AIR_whole.xlsx',sheetname='Sheet3')
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to武汉_TRAIN_AIR_whole.xlsx',sheetname='Sheet4')
#
# color1=['greenyellow','gold','yellow','palegreen','orange','turquoise','cornflowerblue','hotpink','salmon','deepskyblue','yellowgreen']
#
# a = df.plot(kind='barh', alpha=0.54, stacked=True,color=color1)
#
# # 对应位置上显示数据，思想就是先求累加和，然后位置1的数据添加在位置1的1/2处，
# # 其他的添加到相应位置的累加和 - （相应位置的1/2）,'%.2f%%' % (df.ix[i,j]*100)是设置成百分数形式显示
# for i in range(len(df)):
#     for j in range(len(df.ix[1])):
#         if j == 0:
#             plt.text(df1.ix[i, j] / 2-0.01, i, '%.2f%%' % (df.ix[i, j] * 100),
#                      fontproperties=font, va='center', rotation='horizontal')
#         elif j==3:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.025, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         elif j==4:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.025, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         elif j==5:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.032, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         elif j==6:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.021, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         elif j==7:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.0035, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         else:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j]-0.01, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#
# plt.xlim((0.0, 1.0))
# plt.ylim(-0.5,4.5)
#
# plt.legend((u'T1', u'T2', u'T3', u'T4',u'T5',u'A1',u'A2',u'A3',u'A4',u'A5',u'A6'),
#            loc='lower center', prop=font2, ncol=1,bbox_to_anchor=(1.043, 0.12))
#
# plt.xticks(np.arange(0.0,
#                      1.1,
#                      0.2),
#            [u'0.00%',
#             u'20.00%',
#             u'40.00%',
#             u'60.00%',
#             u'80.00%',
#             u'100.00%'],
#            fontproperties=font2)
# plt.yticks(np.arange(0,5,1), [u'分阶段估计法', u'同时估计法',
#                                 u'同时与分阶段结合', u'MNL模型',u'实际结果'], fontproperties=font2)
# plt.show()

"""北京-长沙 各类方法每类产品分担率堆积条形图"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to长沙_TRAIN_AIR_whole.xlsx',sheetname='Sheet3')
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\北京to长沙_TRAIN_AIR_whole.xlsx',sheetname='Sheet4')
#
# color1=['greenyellow','gold','yellow','palegreen','orange','turquoise','cornflowerblue','salmon','deepskyblue','yellowgreen']
#
# a = df.plot(kind='barh', alpha=0.54, stacked=True,color=color1)
#
# # 对应位置上显示数据，思想就是先求累加和，然后位置1的数据添加在位置1的1/2处，
# # 其他的添加到相应位置的累加和 - （相应位置的1/2）,'%.2f%%' % (df.ix[i,j]*100)是设置成百分数形式显示
# for i in range(len(df)):
#     for j in range(len(df.ix[1])):
#         if j == 0:
#             plt.text(df1.ix[i, j] / 2-0.016, i, '%.2f%%' % (df.ix[i, j] * 100),
#                      fontproperties=font, va='center', rotation='horizontal')
#         elif j==4:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j] - 0.004, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#         else:
#             plt.text(-(df.ix[i, j] / 2) + df1.ix[i, j]-0.017, i, '%.2f%%' %
#                      (df.ix[i, j] * 100), fontproperties=font, va='center', rotation='horizontal')
#
# plt.xlim((0.0, 1.0))
# plt.ylim(-0.5,4.5)
#
# plt.legend((u'T1', u'T2', u'T3', u'T4',u'T5',u'A1',u'A2',u'A3',u'A4'),
#            loc='lower center', prop=font2, ncol=1,bbox_to_anchor=(1.043, 0.285))
#
# plt.xticks(np.arange(0.0,
#                      1.1,
#                      0.2),
#            [u'0.00%',
#             u'20.00%',
#             u'40.00%',
#             u'60.00%',
#             u'80.00%',
#             u'100.00%'],
#            fontproperties=font2)
# plt.yticks(np.arange(0,5,1), [u'分阶段估计法', u'同时估计法',
#                                 u'同时与分阶段结合', u'MNL模型',u'实际结果'], fontproperties=font2)
# plt.show()

""" 典型OD的选择参数对比"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\同时估计与分阶段估计相结合的方法的参数结果值.xlsx',sheetname='Sheet1')
#
# fig,ax1 = plt.subplots()
# width=0.7
# # plt.style.use('ggplot')
# ax1.bar(np.arange(-0.5,14,3.5), df[u'上海'], width=0.5, alpha=0.7, color='orange', label=u'北京-上海')
# ax1.bar(np.arange(0,15,3.5),df[u'武汉'],width=0.5,alpha=0.7,color='hotpink',label=u'北京-武汉')
# ax1.bar(np.arange(0.5,15,3.5),df[u'西安'],width=0.5,alpha=0.8,color='greenyellow',label=u'北京-西安')
# ax1.bar(np.arange(1,16,3.5),df[u'长沙'],width=0.5,alpha=0.7,color='cornflowerblue',label=u'北京-长沙')
# ax1.bar(np.arange(1.5,16,3.5),df[u'哈尔'],width=0.5,alpha=0.7,color='aquamarine',label=u'北京-哈尔滨')
#
# ax1.legend(prop=font1,loc='best',shadow=True)
# # ax1.set_xlabel(u'运输方式',fontproperties=font)
# ax1.set_ylabel(u'参数值',fontproperties=font)
# ax1.set_ylim((-8.5,2))
# ax1.set_xlim((-1,16.5))
# plt.yticks(fontproperties=font1)
# plt.xticks(np.arange(0.5,15,3.5),[u'出发时段1',u'到达时段3',u'运行时间',u'票价',
#                                   u'停站数',],fontproperties=font1)   # 字体变成垂直排列，加参数rotation
# plt.show()

""" 典型OD的高铁与航空整体分担率对比"""
# df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\'
#                  u'论文中用到的最终所有每类概率总结_T_A\\典型OD整体分担率对比.xlsx',sheetname='Sheet1')
#
# fig,ax1 = plt.subplots()
# width=0.7
# # plt.style.use('ggplot')
# ax1.bar(np.arange(-0.5,8,2), df[u'高铁'], width=0.5, alpha=0.7, color='gold', label=u'高铁')
# ax1.bar(np.arange(0,8.5,2),df[u'航空'],width=0.5,alpha=0.7,color='palegreen',label=u'航空')
#
# ax1.legend(prop=font1,loc='best',shadow=True)
# # ax1.set_xlabel(u'典型OD',fontproperties=font)
# ax1.set_ylabel(u'分担率',fontproperties=font)
# ax1.set_ylim((0.3,0.71))
# ax1.set_xlim((-1,9))
# plt.yticks(fontproperties=font1)
# plt.xticks(np.arange(0,8.5,2),[u'北京-上海',u'北京-武汉',u'北京-西安',u'北京-长沙',
#                                   u'北京-哈尔滨',],fontproperties=font1)   # 字体变成垂直排列，加参数rotation
# plt.show()





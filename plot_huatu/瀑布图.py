# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from pylab import mpl

font=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=16)
font1=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=14)
font2=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=18)
font3=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=11)
font4=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=13)
font5=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=16)
font6=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=20)
font7=FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc',
    size=14)

mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.style.use('seaborn-white')


"""北京-上海 单一时间_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','yellow','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
#
# ax1.set_ylim(( -0.015,0.011))
# ax1.set_yticklabels(['-.45','-.30','-.15','.00','.15','.30'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1时间变化时各分担率变化量', fontproperties=font6)
#
# # ax1.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
# # ax1.yaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
# # ax1.grid(False)
# # ax1.legend(loc=(2.1,0.0))
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
#
# ax3.set_yticklabels(['-.40','-.32','-.24','-.16','-.08','.00','.08','.16','.24','.32'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][2],df1['PT2'][2],df1['PT3'][2],df1['PT4'][2],df1['PT5'][2],
# df1['PT6'][2],df1['PT7'][2],df1['PA1'][2],df1['PA2'][2],df1['PA3'][2],
# df1['PA4'][2],df1['PA5'][2],df1['PA6'][2],df1['PA7'][2],df1['PA8'][2]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
#
# # total1 = trans1.sum().amount1
# # trans1.loc["net"] = total1
# # blank1.loc["net"] = total1
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
# # step1[1::3] = np.nan
# # blank1.loc["net"] = 0
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.000,0.007))
# my_plot1.set_yticklabels(['.00','.03','.06','.09','.12','.15','.18','.21'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
# # ax2.invert_yaxis()
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
#
# # total2 = trans2.sum().amount2
# # trans2.loc["net"] = total2
# # blank2.loc["net"] = total2
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
# # step2[1::3] = np.nan
# # blank2.loc["net"] = 0
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0020,0.0020))
# my_plot2.set_yticklabels(['-.02','.00','.02','.04','.06','.08','.10','.12','.14'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-上海 单一时间_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','yellow','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 18))
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.060','-.045','-.030','-.015','.000','.015','.030','.045','.060'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# my_plot1.set_yticklabels(['-.006','-.003','.000','.003','.006','.009','.012','.015','.018','.021'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_yticklabels(['-.030','-.015','.000','.015','.030','.045','.060'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-上海 单一时间_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
#                  u'\\北京to上海_单一时间__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.20','-.15','-.10','-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T6时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# ax2.set_ylim((-0.0006,0.0010))
# my_plot1.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04','.05'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_yticklabels(['-.030','-.024','-.018','-.012','-.006','.000','.006','.012','.018','.024'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T6分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-上海 单一时间_7_所有  折线图和瀑布图"""
df0=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
                  u'\\北京to上海_单一时间__画图_7(2).xlsx')
df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
                 u'\\北京to上海_单一时间__画图_7.xlsx')
df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一时间变化_画图'
                 u'\\北京to上海_单一时间__画图_8.xlsx')
fig = plt.figure()
plt.subplots_adjust(wspace=0.1)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

####### 第0个瀑布图 ###########
color0=[ 'yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen','orange',
        'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
index0 = [u'T1', u'T2',u'T3',u'T4',u'T5',
         u'T6',u'T7',u'A1',u'A2',u'A3',
         u'A4',u'A5',u'A6',u'A7',u'A8']
data0 = {'amount1': [df0['PT1'][4],df0['PT2'][4],df0['PT3'][4],df0['PT4'][4],df0['PT5'][4],
df0['PT6'][4],df0['PT7'][4],df0['PA1'][4],df0['PA2'][4],df0['PA3'][4],
df0['PA4'][4],df0['PA5'][4],df0['PA6'][4],df0['PA7'][4],df0['PA8'][4]]}

trans0 = pd.DataFrame(data=data0, index=index0)
blank0 = trans0.amount1.cumsum().shift(1).fillna(0)
step0 = blank0.reset_index(drop=True).repeat(3).shift(-1)

my_plot0 = trans0.plot(kind='bar',ax=ax1, stacked=True, bottom=blank0, legend=None,width=0.5,alpha=1,color=color0)
my_plot0.plot(step0.index, step0.values,'red',linewidth=0.2)
ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
my_plot0.set_ylim((-0.00015,0.00025))
my_plot0.set_yticklabels(['-.015','-.010','-.005','.000','.005','.010','.015','.020','.025'],fontproperties=font5)
my_plot0.set_xticklabels(trans0.index, rotation=0,fontproperties=font5)
ax1.set_title(u'T7分担率减少的瀑布图', fontproperties=font6)


####### 第1个折线图 ###########
color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
        'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.008','-.006','-.004','-.002','.000','.002','.004','.006','.008'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T7时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)


####### 第2个折线图 ###########
p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
         'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)

ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_ylim((-0.004,0.004))
ax3.set_yticklabels(['-.125','-.100','-.075','-.050','-.025','.000','.025','.050','.075','.100'],fontproperties=font5)

ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
ax3.set_title(u'高铁产品时间变化时各分担率变化量', fontproperties=font6)
ax3.legend(loc=(-100,-100))

####### 第1个瀑布图 ###########
color2=['orange','orange','orange','orange','orange','orange','yellowgreen',
        'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
         u'T6',u'T7',u'A1',u'A2',u'A3',
         u'A4',u'A5',u'A6',u'A7',u'A8']
data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}

trans1 = pd.DataFrame(data=data1, index=index1)
blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)

my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# my_plot1.set_ylim((0.0000,0.0035))
my_plot1.set_yticklabels(['-.015','-.010','-.005','.000','.005','.010','.020'],fontproperties=font5)
my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
ax2.set_title(u'T7分担率增加的瀑布图', fontproperties=font6)

####### 第2个瀑布图 ###########
color3=['yellowgreen','yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen','orange',
        'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
         u'T6',u'T7',u'A1',u'A2',u'A3',
         u'A4',u'A5',u'A6',u'A7',u'A8']
data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}

trans2 = pd.DataFrame(data=data2, index=index2)
blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)

my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
my_plot2.set_ylim((0.0000,0.0035))
my_plot2.set_yticklabels(['.00','.03','.06','.09','.12','.15','.18','.21'],fontproperties=font5)
my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)

plt.show()

"""北京-上海 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
#
# ax1.set_ylim(( -0.10,0.15))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_ylim((-0.04,0.08))
# ax3.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.06))
# my_plot1.set_yticklabels(['.00','.01','.02','.03','.04','.05','.06'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1票价变化的瀑布图', fontproperties=font6)
# # ax2.invert_yaxis()
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.005,0.035))
# my_plot2.set_yticklabels(['-.005','.000','.005','.010','.015','.020','.025','.030','.035'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2票价变化的瀑布图', fontproperties=font6)
#
# plt.show()

"""北京-上海 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.02','-.01','-.00','.01','.02','.03'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04','.05'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# my_plot1.set_yticklabels(['-.004','-.002','.000','.002','.004','.006','.008','.010','.012'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_yticklabels(['-.005','.000','.005','.010','.015','.020'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-上海 单一票价_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04','.05','06'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.015','-.010','-.005','.000','.005','.010','.015','.020','.025','030'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T6票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# my_plot1.set_yticklabels(['-.010','-.005','.000','.005','.010','.015','.020','.025'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_yticklabels(['-.010','-.008','-.006','-.004','-.002','.000','.002','.004','.006'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T6分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-上海 单一票价_7_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_7.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to上海\\单一票价变化_画图'
#                  u'\\北京to上海_单一票价__画图_8.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon','plum','orchid']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax1.set_yticklabels(['-.015','-.010','-.005','.000','.005','.010','.015','.020','.025'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T7票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=5,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4','PA5','PA6','PA7','PA8',]].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax3.set_ylim((-0.004,0.004))
# ax3.set_yticklabels(['-.04','-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁产品票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PT6'][4],df1['PT7'][4],df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4],df1['PA7'][4],df1['PA8'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.2)
# # my_plot1.set_ylim((0.000,0.030))
# my_plot1.set_yticklabels(['-.008','-.006','-.004','-.002','.000','.002','.004','.006'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T7分担率变化的瀑布图', fontproperties=font6)
#
# ####### 第2个瀑布图 ###########
# color3=['yellowgreen','yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'T6',u'T7',u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6',u'A7',u'A8']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PT6'][4],df2['PT7'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4],df2['PA7'][4],df2['PA8'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.27)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((0.000,0.030))
# my_plot2.set_yticklabels(['.00','.03','.06','.09','.12','.15','.18'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-哈尔 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to哈尔\\单一票价变化_画图'
#                  u'\\北京to哈尔_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to哈尔\\单一票价变化_画图'
#                  u'\\北京to哈尔_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','khaki','cyan','turquoise','sandybrown','salmon','pink']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
#
# # ax1.set_ylim(( -0.10,0.15))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax3.set_ylim((-0.04,0.08))
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'A1',u'A2',u'A3',
#          u'A4',u'A5']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.12))
# my_plot1.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1票价变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((-0.02,0.10))
# my_plot2.set_yticklabels(['-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2票价变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-哈尔 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to哈尔\\单一票价变化_画图'
#                  u'\\北京to哈尔_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to哈尔\\单一票价变化_画图'
#                  u'\\北京to哈尔_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','orange','cyan','turquoise','sandybrown','salmon','pink']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
#
# ax1.set_ylim(( -0.14,0.25))
# ax1.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax3.set_ylim((-0.10,0.20))
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'A1',u'A2',u'A3',
#          u'A4',u'A5']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((-0.06,0.08))
# my_plot1.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3票价变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.06,0.04))
# my_plot2.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4票价变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-哈尔 单一票价_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to哈尔\\单一票价变化_画图'
#                  u'\\北京to哈尔_单一票价__画图_5.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','orange','cyan','turquoise','sandybrown','salmon','pink']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
#
# # ax1.set_ylim(( -0.14,0.25))
# ax1.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'高铁票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第1个瀑布图 ###########
# color2=[ 'yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'A1',u'A2',u'A3',
#          u'A4',u'A5']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((-0.06,0.08))
# my_plot1.set_yticklabels(['-.02','.00','.02','.04','.06','.10','.12','.14'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax2.set_title(u'高铁票价变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一时间_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一时间变化_画图'
#                  u'\\北京to西安_单一时间__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一时间变化_画图'
#                  u'\\北京to西安_单一时间__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax1.set_ylim(( -0.15,0.10))
# ax1.set_yticklabels(['-.15','-.10','-.05','.00','.05'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_ylim((-0.15,0.25))
# ax3.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][1],df1['PT2'][1],df1['PT3'][1],df1['PT4'][1],
# df1['PA1'][1],df1['PA2'][1],df1['PA3'][1],
# df1['PA4'][1],df1['PA5'][1],df1['PA6'][1]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.06))
# my_plot1.set_yticklabels(['.000','.015','.030','.045','.060','.075','.090'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][2],df2['PT2'][2],df2['PT3'][2],df2['PT4'][2],
# df2['PA1'][2],df2['PA2'][2],df2['PA3'][2],
# df2['PA4'][2],df2['PA5'][2],df2['PA6'][2]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.04,0.14))
# my_plot2.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08','.10','.12','.14'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一时间_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一时间变化_画图'
#                  u'\\北京to西安_单一时间__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一时间变化_画图'
#                  u'\\北京to西安_单一时间__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][1],df1['PT2'][1],df1['PT3'][1],df1['PT4'][1],
# df1['PA1'][1],df1['PA2'][1],df1['PA3'][1],
# df1['PA4'][1],df1['PA5'][1],df1['PA6'][1]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][2],df2['PT2'][2],df2['PT3'][2],df2['PT4'][2],
# df2['PA1'][2],df2['PA2'][2],df2['PA3'][2],
# df2['PA4'][2],df2['PA5'][2],df2['PA6'][2]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一时间_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一时间变化_画图'
#                  u'\\北京to西安_单一时间__画图_5.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.20','-.15','-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'高铁时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
# ####### 第1个瀑布图 ###########
# color2=[ 'yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][1],df1['PT2'][1],df1['PT3'][1],df1['PT4'][1],
# df1['PA1'][1],df1['PA2'][1],df1['PA3'][1],
# df1['PA4'][1],df1['PA5'][1],df1['PA6'][1]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14','.16'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax2.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一票价变化_画图'
#                  u'\\北京to西安_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一票价变化_画图'
#                  u'\\北京to西安_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.08))
# my_plot1.set_yticklabels(['.000','.010','.020','.030','.040','.050','.060','.070','.080'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.020','-.010','.000','.010','.020','.030','.040','.050','.060'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一票价变化_画图'
#                  u'\\北京to西安_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一票价变化_画图'
#                  u'\\北京to西安_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.030','-.015','.000','.015','.030','.045'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.04','-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-西安 单一票价_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to西安\\单一票价变化_画图'
#                  u'\\北京to西安_单一票价__画图_5.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)
#
# ####### 第1个折线图 ###########
# color1=['springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.10','-.08','-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'高铁票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
# ####### 第1个瀑布图 ###########
# color2=[ 'yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['.000','.030','.060','.090','.120','.150','.180'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax2.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()



"""北京-武汉 单一时间_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.20','-.15','-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][1],df1['PT2'][1],df1['PT3'][1],df1['PT4'][1],df1['PT5'][1],
# df1['PA1'][1],df1['PA2'][1],df1['PA3'][1],
# df1['PA4'][1],df1['PA5'][1],df1['PA6'][1]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14','.16','.18'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.02','.00','.02','.04','.06','.08','.10','.12','.14','.16'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-武汉 单一时间_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.20','-.10','.00','.10','.20','.30','.40'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25','.30','.35'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][3],df1['PT2'][3],df1['PT3'][3],df1['PT4'][3],df1['PT5'][3],
# df1['PA1'][3],df1['PA2'][3],df1['PA3'][3],
# df1['PA4'][3],df1['PA5'][3],df1['PA6'][3]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0020,0.0020))
# my_plot2.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-武汉 单一时间_5_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一时间变化_画图'
#                  u'\\北京to武汉_单一时间__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# # ax1.set_ylim(( -0.1,0.31))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25','.30'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 18))
# # ax3.set_ylim((-0.06,0.081))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.09','-.06','-.03','.00','.03','.06','.09'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][3],df1['PT2'][3],df1['PT3'][3],df1['PT4'][3],df1['PT5'][3],
# df1['PA1'][3],df1['PA2'][3],df1['PA3'][3],
# df1['PA4'][3],df1['PA5'][3],df1['PA6'][3]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((0.00,0.08))
# my_plot2.set_yticklabels(['.00','.02','.04','.06','.08','.010','.012','.014','.016'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-武汉 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5,],fontproperties=font5)
# # ax1.set_ylim(( -0.10,0.16))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5,],fontproperties=font5)
# ax3.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.07))
# my_plot1.set_yticklabels(['.00','.01','.02','.03','.04','.05','.06','.07'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.02,0.03))
# my_plot2.set_yticklabels(['-.005','.000','.005','.010','.015','.020','.025','.030','.035','.040'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-武汉 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0,20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.10,0.15))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 20.1))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04','.05','.06'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((-0.04,0.031))
# my_plot1.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.024,0.011))
# my_plot2.set_yticklabels(['-.018','-.012','-.006','.000','.006','.012','.018'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-武汉 单一票价_5_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to武汉\\单一票价变化_画图'
#                  u'\\北京to武汉_单一票价__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
# # plt.style.use('classic')
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'cyan','deepskyblue','turquoise','cornflowerblue','hotpink','salmon']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 20))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.04,0.08))
# ax1.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4','PA5','PA6']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 20))
# # ax3.set_ylim((-0.006,0.008))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4],df1['PA5'][4],df1['PA6'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.025','-.020','-.015','-.010','-.005','.000','.005','.010','.015'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon','salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4',u'A5',u'A6']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4],df2['PA5'][4],df2['PA6'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((0.00,0.06))
# my_plot2.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一时间_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax1.set_ylim(( -0.008,0.006))
# ax1.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax3.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][3],df1['PT2'][3],df1['PT3'][3],df1['PT4'][3],df1['PT5'][3],df1['PT6'][3],df1['PT7'][3],
# df1['PA1'][3],df1['PA2'][3],df1['PA3'][3],
# df1['PA4'][3]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['.000','.005','.010','.015','.020','.025','.030','.035'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],df2['PT6'][3],df2['PT7'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['-.020','-.010','.000','.010','.020','.030','.040','.050'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一时间_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# # ax1.set_ylim(( -0.0051,0.0041))
# ax1.set_yticklabels(['-.05','-.04','-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax3.set_yticklabels(['-.04','-.03','-.02','-.01','.00','.01','.02','.03'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][3],df1['PT2'][3],df1['PT3'][3],df1['PT4'][3],df1['PT5'][3],df1['PT6'][3],df1['PT7'][3],
# df1['PA1'][3],df1['PA2'][3],df1['PA3'][3],
# df1['PA4'][3]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((-0.0010,0.00151))
# my_plot1.set_yticklabels(['-.030','-.015','.000','.015','.030','.045'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],df2['PT6'][3],df2['PT7'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.015','-.012','-.009','-.006','-.003','.000','.003','.006','.009','.012'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一时间_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 18))
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax3.set_yticklabels(['-.015','-.010','-.005','.000','.005','.010','.015'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T6时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],df1['PT6'][4],df1['PT7'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.04','-.03','-.02','-.01','.00','.01','.02'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],df2['PT6'][3],df2['PT7'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.010','-.008','-.006','-.004','-.002','.000','.002','.004'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T6分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一时间_7_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_7.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一时间变化_画图'
#                  u'\\北京to南京_单一时间__画图_8.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 22))
# ax1.set_xticklabels([0.4,0.65,0.9,1.15,1.4],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T7时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.12','-.09','-.06','-.03','.00','.03','.06','.09','.12'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][8],df1['PT2'][8],df1['PT3'][8],df1['PT4'][8],df1['PT5'][8],df1['PT6'][8],df1['PT7'][8],
# df1['PA1'][8],df1['PA2'][8],df1['PA3'][8],
# df1['PA4'][8]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.03','-.02','-.01','.00','.01'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T7分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],df2['PT6'][4],df2['PT7'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['.00','.03','.06','.09','.12','.15','.18'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()



"""北京-南京 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax1.set_ylim(( -0.15,0.25))
# ax1.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_ylim((-0.15,0.25))
# ax3.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],df1['PT6'][4],df1['PT7'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.14))
# my_plot1.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],df2['PT6'][4],df2['PT7'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# my_plot2.set_ylim((-0.02,0.10))
# my_plot2.set_yticklabels(['-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.0051,0.0041))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06','.08','.10','.12'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],df1['PT6'][4],df1['PT7'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04','.05'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],df2['PT6'][4],df2['PT7'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一票价_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 18))
# ax1.set_xticklabels([0.50,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.02','-.01','.00','.01','.02','.03','.04','.05'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T6票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],df1['PT6'][4],df1['PT7'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((-0.06,0.041))
# my_plot1.set_yticklabels(['-.09','-.06','-.03','.00','.03','.06'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],df2['PT6'][4],df2['PT7'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['-.018','-.012','-.006','.000','.006','.012'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T6分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-南京 单一票价_7_所有  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_7.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to南京\\单一票价变化_画图'
#                  u'\\北京to南京_单一票价__画图_8.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','gold','springgreen','mediumseagreen','goldenrod','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 22))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.020,0.010))
# ax1.set_yticklabels(['-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T7票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5','PT6','PT7',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.09','-.06','-.03','.00','.03','.06','.09','.12'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],df1['PT6'][4],df1['PT7'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0,0.0035))
# my_plot1.set_yticklabels(['-.018','-.015','-.012','-.009','-.006','-.003','.000','.003','.006','.009'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T7分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['yellowgreen', 'yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',u'T6',u'T7',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],df2['PT6'][4],df2['PT7'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.10,0.21))
# my_plot2.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一时间_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 15))
# ax1.set_xticklabels([0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax1.set_ylim(( -0.15,0.151))
# ax1.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 17))
# ax3.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20','.25'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][1],df1['PT2'][1],df1['PT3'][1],df1['PT4'][1],df1['PT5'][1],
# df1['PA1'][1],df1['PA2'][1],df1['PA3'][1],
# df1['PA4'][1]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一时间_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.008,0.006))
# ax1.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08','.10','.12'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 17))
# ax3.set_xticklabels([0.65,0.75,0.85,0.95,1.05,1.15,1.25,1.35,1.45],fontproperties=font5)
# ax3.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][2],df1['PT2'][2],df1['PT3'][2],df1['PT4'][2],df1['PT5'][2],
# df1['PA1'][2],df1['PA2'][2],df1['PA3'][2],df1['PA4'][2]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['-.03','-.02','-.01','.00','.01','.02','.03','.04'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['-.08','-.06','-.04','-.02','.00','.02','.04'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一时间_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一时间变化_画图'
#                  u'\\北京to长沙_单一时间__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax1.set_xlim((0, 18))
# ax1.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.008,0.006))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15','.20'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5时间变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# ax3.set_xlim((0, 18))
# ax3.set_xticklabels([0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.09','-.06','-.03','.00','.03','.06','.09'],fontproperties=font5)
#
# ax3.set_xlabel(u"运行时间变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁时间变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['-.04','-.03','-.02','-.01','.00','.01'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一票价_1_2  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_1.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_2.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.008,0.006))
# ax1.set_yticklabels(['-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T1票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06','.08','.10'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T2票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=['yellowgreen', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# my_plot1.set_ylim((0.00,0.08))
# my_plot1.set_yticklabels(['.00','.01','.02','.03','.04','.05','.06','.07','.08'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T1分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange','yellowgreen', 'orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['-.02','-.01','.00','.01','.02','.03','.04','.05'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T2分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一票价_3_4  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_3.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_4.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax1.set_ylim(( -0.02,0.06))
# ax1.set_yticklabels(['-.030','-.015','.000','.015','.030','.045','.060','.075','.090'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T3票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.060','-.040','-.020','.000','.020','.040','.060','.080','.100'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'T4票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','yellowgreen','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['-.030','-.020','-.010','.000','.010','.020','.030','.040'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T3分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','yellowgreen','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][3],df2['PT2'][3],df2['PT3'][3],df2['PT4'][3],df2['PT5'][3],
# df2['PA1'][3],df2['PA2'][3],df2['PA3'][3],
# df2['PA4'][3]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['-.06','-.04','-.02','.00','.02','.04','.06'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'T4分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


"""北京-长沙 单一票价_5_6  折线图和瀑布图"""
# df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_5.xlsx')
# df2=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\北京to长沙\\单一票价变化_画图'
#                  u'\\北京to长沙_单一票价__画图_6.xlsx')
# fig = plt.figure()
# plt.subplots_adjust(wspace=0.1)
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
#
#
# ####### 第1个折线图 ###########
# color1=['greenyellow','springgreen','mediumseagreen','yellowgreen','orange',
#         'deepskyblue','turquoise','hotpink','plum']
#
# p1 = df1[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax1,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax1.set_xlim((0, 16))
# ax1.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# # ax1.set_ylim(( -0.008,0.006))
# ax1.set_yticklabels(['-.04','-.02','.00','.02','.04','.06','.08'],fontproperties=font5)
#
# ax1.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax1.set_title(u'T5票价变化时各分担率变化量', fontproperties=font6)
#
# ax1.legend(loc='best', ncol=3,prop=font7)
#
#
# ####### 第2个折线图 ###########
# p3 = df2[['PT1','PT2','PT3','PT4','PT5',
#          'PA1','PA2','PA3','PA4']].plot(kind='line',
# ax=ax3,color=color1,alpha=1,marker='o',linewidth=1.5)
#
# # ax3.set_xlim((0, 16))
# ax3.set_xticklabels([0.5,0.75,1,1.25,1.5],fontproperties=font5)
# ax3.set_yticklabels(['-.15','-.10','-.05','.00','.05','.10','.15'],fontproperties=font5)
#
# ax3.set_xlabel(u"票价变化倍数",fontproperties=font6)
# ax3.set_ylabel(u"分担率变化量",fontproperties=font6)
# ax3.set_title(u'高铁票价变化时各分担率变化量', fontproperties=font6)
# ax3.legend(loc=(-100,-100))
#
# ####### 第1个瀑布图 ###########
# color2=[ 'orange','orange','orange','orange','yellowgreen',
#         'salmon', 'salmon', 'salmon','salmon']
# index1 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#         u'A1',u'A2',u'A3',
#          u'A4']
# data1 = {'amount1': [df1['PT1'][4],df1['PT2'][4],df1['PT3'][4],df1['PT4'][4],df1['PT5'][4],
# df1['PA1'][4],df1['PA2'][4],df1['PA3'][4],
# df1['PA4'][4]]}
#
# trans1 = pd.DataFrame(data=data1, index=index1)
# blank1 = trans1.amount1.cumsum().shift(1).fillna(0)
# step1 = blank1.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot1 = trans1.plot(kind='bar',ax=ax2, stacked=True, bottom=blank1, legend=None,width=0.5,alpha=1,color=color2)
# my_plot1.plot(step1.index, step1.values,'red',linewidth=0.25)
# # my_plot1.set_ylim((0.0000,0.0035))
# my_plot1.set_yticklabels(['-.02','-.01','.00','.01','.02'],fontproperties=font5)
# my_plot1.set_xticklabels(trans1.index, rotation=0,fontproperties=font5)
# ax2.set_title(u'T5分担率变化的瀑布图', fontproperties=font6)
#
#
# ####### 第2个瀑布图 ###########
# color3=['orange', 'orange','orange','orange','orange',
#         'salmon', 'salmon', 'salmon','salmon']
# index2 = [u'T1', u'T2',u'T3',u'T4',u'T5',
#          u'A1',u'A2',u'A3',
#          u'A4']
# data2 = {'amount2': [df2['PT1'][4],df2['PT2'][4],df2['PT3'][4],df2['PT4'][4],df2['PT5'][4],
# df2['PA1'][4],df2['PA2'][4],df2['PA3'][4],
# df2['PA4'][4]]}
#
# trans2 = pd.DataFrame(data=data2, index=index2)
# blank2 = trans2.amount2.cumsum().shift(1).fillna(0)
# step2 = blank2.reset_index(drop=True).repeat(3).shift(-1)
#
# my_plot2 = trans2.plot(kind='bar',ax=ax4, stacked=True, bottom=blank2, legend=None,width=0.5,alpha=1,color=color3)
# my_plot2.plot(step2.index, step2.values,'red',linewidth=0.25)
# my_plot2.set_xlabel(u"产品类别",fontproperties=font6)
# # my_plot2.set_ylim((-0.0010,0.0025))
# my_plot2.set_yticklabels(['.00','.02','.04','.06','.08','.10','.12','.14','.06'],fontproperties=font5)
# my_plot2.set_xticklabels(trans2.index, rotation=0,fontproperties=font5)
# ax4.set_title(u'高铁分担率变化的瀑布图', fontproperties=font6)
#
# plt.show()


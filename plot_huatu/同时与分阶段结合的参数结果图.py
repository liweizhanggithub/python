# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
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
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.style.use('seaborn-white')

"""
参数结果条形图
"""
df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\同时估计与分阶段估计相结合的方法的参数结果值.xlsx',sheetname=0)
### 注意，sheetname=0是北京-上海的的参数结果，sheetname=1是北京-哈尔的参数结果，以此类推############

df1 = df[[u'参数', u'Estimate']]

df1.plot(kind='bar',alpha=0.7,width=0.5,color='cornflowerblue',legend=False)
plt.ylabel(u'参数估计值', fontproperties=font)
plt.ylim((-9,2))
plt.xticks(np.arange(len(df)), df[u'参数'], fontproperties=font1)
plt.yticks(fontproperties=font1)
plt.show()
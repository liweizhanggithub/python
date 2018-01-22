# -*- coding: utf-8 -*-
"""
整理各个OD 的单一时间变化、单一票价变化数据，为画单因素变化图准备数据
具体是 将每个数据减去 什么都不变化的 概率值，得到对应变化因素下对应的概率差值，为画瀑布图、折线图做准备‘
之所以要进行差值画图，是因为有些概率值很小，直接画概率图，变化的效果不明显
"""
import pandas as pd

def single_factor(o1,d1,train):
    """

    :param o1: O
    :param d1: D
    :param t: 数字，表示高铁类别
    :return:
    """
    for x in range(1,train+1):
        """单一时间画图数据的整理"""
        dfx=pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\%sto%s\\单一时间变化\\%sto%s_单一时间_%s.csv'
                       % (o1,d1,o1,d1,x))

        """ 求得高铁的类数、航空的类数"""
        t_count=0
        a_count=0
        for name in dfx.columns[1:]:
            if 'n' in name:
                t_count+=1
            else:
                a_count+=1

        """ 取出高铁中每类什么都不做改变的概率值、航空中每类什么都不做改变的概率值，即对应倍数为1时的每类概率"""
        t_data=[]
        a_data=[]
        for i in range(1,t_count+1):
            a=dfx[dfx['multiple']==1]['Ptrainlist%s' % (i)].values
            t_data.append(a)

        for j in range(1,a_count+1):
            b=dfx[dfx['multiple']==1]['Pairlist%s' % (j)].values
            a_data.append(b)

        """ 将上步取出的对应倍数为1时的每类概率加入到DataFrame中，方便后步直接相减求概率差值"""
        for m in range(1,t_count+1):
            dfx['pt%s' % (m)]=float(t_data[m-1])

        for n in range(1,a_count+1):
            dfx['pa%s' % (n)]=float(a_data[n-1])

        """ 对高铁每类、航空每类的所有概率分别对应减去相应倍数为1的概率，求得概率差值"""
        for k in range(1,t_count+1):
            dfx['PT%s' % (k)]=dfx['Ptrainlist%s'% (k)]-dfx['pt%s' % (k)]

        for l in range(1,a_count+1):
            dfx['PA%s' % (l)]=dfx['Pairlist%s'% (l)]-dfx['pa%s' % (l)]

        dfx.to_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\%sto%s\\单一时间变化_画图\\%sto%s_单一时间__画图_%s.xlsx'
                    % (o1,d1,o1,d1,x))
#############################################################################################################

    for y in range(1,train+1):
        """单一票价画图数据的整理"""
        ddy = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\%sto%s\\单一票价变化\\%sto%s_单一票价_%s.csv'
                         % (o1, d1, o1, d1, y))

        """ 求得高铁的类数、航空的类数"""
        t1_count=0
        a1_count=0
        for name1 in ddy.columns[1:]:
            if 'n' in name1:
                t1_count+=1
            else:
                a1_count+=1

        """ 取出高铁中每类什么都不做改变的概率值、航空中每类什么都不做改变的概率值，即对应倍数为1时的每类概率"""
        t1_data=[]
        a1_data=[]
        for ii in range(1,t1_count+1):
            a1=ddy[ddy['multiple']==1]['Ptrainlist%s' % (ii)].values
            t1_data.append(a1)

        for jj in range(1,a1_count+1):
            b1=ddy[ddy['multiple']==1]['Pairlist%s' % (jj)].values
            a1_data.append(b1)

        """ 将上步取出的对应倍数为1时的每类概率加入到DataFrame中，方便后步直接相减求概率差值"""
        for mm in range(1, t1_count + 1):
            ddy['pt%s' % (mm)] = float(t1_data[mm - 1])

        for nn in range(1, a1_count + 1):
            ddy['pa%s' % (nn)] = float(a1_data[nn - 1])

        """ 对高铁每类、航空每类的所有概率分别对应减去相应倍数为1的概率，求得概率差值"""
        for kk in range(1, t1_count + 1):
            ddy['PT%s' % (kk)] = ddy['Ptrainlist%s' % (kk)] - ddy['pt%s' % (kk)]

        for ll in range(1, a1_count + 1):
            ddy['PA%s' % (ll)] = ddy['Pairlist%s' % (ll)] - ddy['pa%s' % (ll)]

        ddy.to_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\%sto%s\\单一票价变化_画图\\%sto%s_单一票价__画图_%s.xlsx'
                    % (o1, d1, o1, d1, y))

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_p_new\\odta.xlsx')

    for data in od.values:
        single_factor(data[0], data[1],data[2])

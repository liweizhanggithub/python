# -*- coding: utf-8 -*-
"""
将刚才 resule_p_arrange,py 的写出的数按照CHO进行升序排列，形成与原始数据对应的顺序，为求弹性值做准备

"""
import pandas as pd

def result_p_arrange_2(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    df=pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\TRAIN_p_new.csv' % (o1,d1))
    df1=df[['code','CHO','PTR.2','PAIR.2','PtrainTR.2','Ptrain.2','PtrainTR_same_stage','Ptrain_same_stage']]
    df11=df1.sort_index(axis=0, ascending=True, by='CHO')
    df12=df11[['code','PTR.2','PAIR.2','PtrainTR.2','Ptrain.2','PtrainTR_same_stage','Ptrain_same_stage']]
    df12.rename(columns={'PTR.2':'PTR_new','PAIR.2':'PAIR_new','PtrainTR_same_stage':'PtrainTR_new','Ptrain_same_stage':'Ptrain_new'},inplace=True)
    df12.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\TRAIN_p_new_new.csv' % (o1,d1),encoding = 'gbk')

    df2=pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\AIR_p_new.csv' % (o1,d1))
    df3=df2[['code','CHO','PTR.2','PAIR.2','PairAIR.2','Pair.2','PairAIR_same_stage','Pair_same_stage']]
    df4=df3.sort_index(axis=0, ascending=True, by='CHO')
    df5=df3[['code','PTR.2','PAIR.2','PairAIR.2','Pair.2','PairAIR_same_stage','Pair_same_stage']]
    df5.rename(columns={'PTR.2':'PTR_new','PAIR.2':'PAIR_new','PairAIR_same_stage':'PairAIR_new','Pair_same_stage':'Pair_new'},inplace=True)
    df5.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\AIR_p_new_new.csv' % (o1,d1),encoding = 'gbk')

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        result_p_arrange_2(data[0], data[1])
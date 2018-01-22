# -*- coding: utf-8 -*-
"""
将 train_air 中的数据整理成画三维图需要的数据形式
即做每一类的三维图，将数据首先是分别按照高铁和航空的分类进行排序，再将高铁和航空合并，高铁在前
这样得到的就是没哟个OD有顺序的数据，比 normal_data_elastic.py 的数据更整齐，
normal_data_elastic.py 的数据只保证高铁的每一类轮流在最前面

"""
import pandas as pd

def data_elastic(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    df=pd.read_csv(u'G:\\zlw_paper_new\\train_air\\excel_normal\\excel_normal_分类\\%sto%s.csv' % (o1,d1))

    df_new=df[['code','TRAFFIC','CON','SAFETY','CONVIENCE','MILE', 'ONTIME0', 'ONTIME1', 'ONTIME2', 'ONTIME3',
                  'OFFTIME0', 'OFFTIME1', 'OFFTIME2', 'OFFTIME3',
                  'TRAINTIME', 'PRICE','SEATTYPE', 'STOPNUM','ZHUNDIANLV','SEAT_CAPACITY','PSGNUM'] ]

    df_TR=df_new[df_new['TRAFFIC']=='train']
    df_AIR=df_new[df_new['TRAFFIC']=='air']

    df_TR1=df_TR.sort_values('code',ascending=True)
    df_AIR1=df_AIR.sort_values('code',ascending=True)

    df_T_A=pd.concat([df_TR1,df_AIR1],axis=0)
    df_T_A1=pd.DataFrame(df_T_A)

    df_T_A1.to_csv(u'G:\\zlw_paper_new\\train_air\\excel_normal'
                           u'\\excel_normal_分类\\%sto%s\\%sto%s_TRAIN.csv' % (o1,d1,o1,d1))

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        data_elastic(data[0], data[1])




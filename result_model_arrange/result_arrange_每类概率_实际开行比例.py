# -*- coding: utf-8 -*-
"""
在 result_arrange_每类概率.py 的基础上，将列车开行数量、列车开行比例链接过来
注意：不知道为什么，北京-上海的实现不了

"""
import pandas as pd

def p_whole(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    df_3 = pd.read_excel(u'G:\\zlw_paper_new\\train_air\\excel_normal\\excel_normal_分类\\excel_normal分类及每类的起止号码.xlsx',
                             sheetname='%s' % (d1))

    df=pd.read_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN_AIR.xlsx' % (o1,d1))

    df['number']=df_3['number']
    df['percent']=df_3['percent']

    df.to_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN_AIR_whole.xlsx' % (o1,d1))

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\od.xlsx')
    for data in od.values:
        p_whole(data[0], data[1])

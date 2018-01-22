# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import openpyxl as xls
import warnings     # python开发中经常遇到报错的情况，但是warning通常并不影响程序的运行，
warnings.filterwarnings("ignore")   # 这两句话就忽略了警告错误的输出
from openpyxl.writer.excel import ExcelWriter
import Connect_to_oracle_188.connect_oracle as oc
from sql_nihe import sql_nihe_you
import pickle as plk
from sklearn import preprocessing  # sklearn是个包，preprocessing 模块提供了数据预处理函数和预处理类
from chapter2.creat_excel_manysheets import creat_excel
from xlutils.copy import copy
from xlrd import open_workbook
import xlsxwriter

def you_prove(o1, d1):
    """
    连接数据库，获取不同OD 的列车产品特性
    1、连接oracle，进行查询

    :param o: O
    :param d: D
    :return:
    """

    """ 1、连接oracle，进行查询"""
    oracle = oc.Oracle()
    df = oracle.query_data(sql_nihe_you % (o1, d1))

    # 将查询结果暂存入本地plk文档中
    oradata = open('you_read.plk', 'wb')    # 以二进制写模式打开文件
    plk.dump(df, oradata)               # 向文件中写入数据
    oradata.close()                    # 关闭文件
    oracle.close_oralce()
    input0 = open('you_read.plk', 'rb')  # 以二进制读模式打开文件
    df = plk.load(input0)

    column1 = ['ONSTATION', 'OFFSTATION','TRAINNO',
               'ONTIME','OFFTIME',
               'PRICE','SEAT_NUM','KEZUOLV']
    df = pd.DataFrame(df,columns=column1)
    print df
    return df

if __name__ == '__main__':
    od_data = pd.read_excel(u'G:\\zlw_paper_new\\拟合数据\\OD.xlsx')
    print od_data
    for data in od_data.values:
        try:
            cc = you_prove(data[0], data[1])
            print cc
            cc.to_excel(u'G:\\zlw_paper_new\\拟合数据\\有验证\\%sto%sto有验证.xlsx' %
                (data[0], data[1]))
        except BaseException:
            pass

# if __name__ == '__main__':
#     od_data = pd.read_excel(u'G:\\zlw_paper_new\\拟合数据\\OD.xlsx')
#     print od_data
#     for data in od_data.values:
#         try:
#             cc = train_seatnum_1(data[0], data[1])
#             print cc
#             data_train = open(
#                 u'G:\\zlw_paper_new\\train_1\\plk\\%sto%sto高铁.plk' %
#                 (data[0], data[1]), 'w')
#             plk.dump(cc, data_train)
#             data_train.close()
#         except BaseException:
#             pass
    # cc = train_seatnum_1(u'北京', u'武汉')
    # data_train = open(
    #     u'G:\\zlw_paper_new\\train_1\\plk\\%sto%sto高铁.plk' %
    #     (u'北京', u'武汉'), 'w')
    # plk.dump(cc, data_train)
    # data_train.close()

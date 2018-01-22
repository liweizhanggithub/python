# -*- coding: utf-8 -*-
"""
注意：
df.to_excel（）是没有文件，会自己新建文件，但是只能写入一次性写入，否则后面写入的会将前面的进行覆盖
"""
import numpy as np
import pandas as pd
import openpyxl as xls
import warnings     # python开发中经常遇到报错的情况，但是warning通常并不影响程序的运行，
warnings.filterwarnings("ignore")   # 这两句话就忽略了警告错误的输出
from openpyxl.writer.excel import ExcelWriter
import Connect_to_oracle_188.connect_oracle as oc
import pickle as plk
from sklearn import preprocessing  # sklearn是个包，preprocessing 模块提供了数据预处理函数和预处理类
from chapter2.creat_excel_manysheets import creat_excel
from xlutils.copy import copy
from xlrd import open_workbook
import xlsxwriter

def train_air_normalization(o1, d1):
    """
    数值型特性变量标准化,包括safety,convience,mile,traintime,price,seattype,stopnum,seat_capacity
    :param o: O
    :param d: D
    :return:  效用函数的特性变量列表
    """
    df=pd.read_excel(u'G:\\zlw_paper_new\\train_air\\excel\\{0}to{1}.xlsx'.format(
        o1, d1))
    df['CON']=1 # 增加一列常数项，计算基本效用

    """对安全性、方便性、旅行时间、坐席等级、票价、停站数进行标准化"""
    df['SAFETY'] = preprocessing.maxabs_scale(
        df['SAFETY']).round(4)
    df['CONVIENCE'] = preprocessing.maxabs_scale(
        df['CONVIENCE']).round(4)
    df['MILE'] = preprocessing.maxabs_scale(
        df['MILE']).round(4)
    df['TRAINTIME'] = preprocessing.maxabs_scale(  # preprocessing.maxabs_scale(X, axis=0, copy=True)：
        # 数据的缩放比例为绝对值最大值，并保留正负号，即在
        # 区间 [-1.0, 1.0] 内。唯一可用于稀疏数据 scipy.sparse 的标准化
        df['TRAINTIME']).round(4)  # round() 方法返回浮点数的四舍五入值，这里是保留4位小数
    df['PRICE'] = preprocessing.maxabs_scale(
        df['PRICE']).round(4)
    df['SEATTYPE'] = preprocessing.maxabs_scale(
        df['SEATTYPE']).round(4)
    df['STOPNUM'] = preprocessing.maxabs_scale(
        df['STOPNUM']).round(4)
    df['SEAT_CAPACITY'] = preprocessing.maxabs_scale(
        df['SEAT_CAPACITY']).round(4)

    column1 = ['CHO', 'ONSTATION', 'OFFSTATION', 'TRAFFIC','CON', 'SAFETY', 'CONVIENCE', 'MILE',
               'ONTIME0', 'ONTIME1', 'ONTIME2', 'ONTIME3', 'OFFTIME0', 'OFFTIME1', 'OFFTIME2', 'OFFTIME3', 'TRAINTIME',
               'PRICE', 'SEATTYPE', 'STOPNUM', 'ZHUNDIANLV', 'SEAT_CAPACITY', 'PSGNUM']
    df = pd.DataFrame(df, columns=column1)
    return df

"第一种方式，直接生成 xlsx 的 Excel 文件"
if __name__ == '__main__':
    """写入到EXCEL文件中"""
    # od_data = pd.read_excel(u'G:\\zlw_paper_new\\train\\ODAIR.xlsx')
    # print od_data
    # for data in od_data.values:
    #     try:
    #         cc = train_air_normalization(data[0], data[1])
    #         print cc
    #         cc1=pd.DataFrame(cc)
    #         cc1.to_excel(u'G:\\zlw_paper_new\\train_air\\excel_normal\\%sto%s.csv' %
    #             (data[0], data[1]))
    #     except BaseException:
    #         pass
    """写入到csv中，但是要加入encoding = 'gbk'，防止中文乱码"""
    od_data = pd.read_excel(u'G:\\zlw_paper_new\\train\\ODAIR.xlsx')
    print od_data
    for data in od_data.values:
        try:
            cc = train_air_normalization(data[0], data[1])
            print cc
            cc1=pd.DataFrame(cc)
            cc1.to_csv(u'G:\\zlw_paper_new\\train_air\\excel_normal\\%sto%s.csv' %
                (data[0], data[1]),encoding = 'gbk')
        except BaseException:
            pass

    # cc = train_air_normalization(u'北京',u'西安')
    # print cc
    # cc.to_csv(u'G:\\zlw_paper_new\\train_air\\excel_normal\\%sto%s.csv' %
    #             (u'北京',u'西安'),encoding = 'gbk')

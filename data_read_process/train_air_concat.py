# -*- coding: utf-8 -*-
"""
将高铁数据与航空数据合并起来，形成总的数据，用到的核心点是 pd.concat 函数
"""
import pandas as pd
import warnings     # python开发中经常遇到报错的情况，但是warning通常并不影响程序的运行，
warnings.filterwarnings("ignore")   # 这两句话就忽略了警告错误的输出
from openpyxl.writer.excel import ExcelWriter
import pickle as plk
from xlutils.copy import copy
from xlrd import open_workbook
import xlsxwriter
import xlwt
import numpy as np
import string

def data_arrange(o1,d1):
    """
    将高铁数据和航空数据写入到同一个EXCEL里面
    :param o:
    :param d:
    :return:
    """
    excel = u'G:\\zlw_paper_new\\train\\excel\\{0}to{1}to高铁.xlsx'.format(
        o1, d1)  # format函数是增强的格式化字符串函数，它通过{}和:来代替%。
    file2 = u'G:\\zlw_paper_new\\air\\excel\\{0}to{1}to航空.xlsx'.format(
        o1, d1)  # format函数是增强的格式化字符串函数，它通过{}和:来代替%。
    df1=pd.read_excel(excel)
    df2=pd.read_excel(file2)
    frames=[df1,df2]
    df3 = pd.concat(frames)
    column1 = ['CHO', 'ONSTATION', 'OFFSTATION', 'TRAFFIC', 'SAFETY', 'CONVIENCE', 'MILE',
               'ONTIME0', 'ONTIME1', 'ONTIME2', 'ONTIME3', 'OFFTIME0', 'OFFTIME1', 'OFFTIME2', 'OFFTIME3', 'TRAINTIME',
               'PRICE', 'SEATTYPE', 'STOPNUM', 'ZHUNDIANLV', 'SEAT_CAPACITY', 'PSGNUM']
    df3=pd.DataFrame(df3,columns=column1)
    df3.reset_index(inplace=True)
    del df3['index']
    print df3
    df3.to_excel(u'G:\\zlw_paper_new\\train_air\\excel\\{0}to{1}.xlsx'.format(o1, d1))

    # # 向已存在的Excel表格里写入数据
    # rb = open_workbook(excel)  # 打开要写入数据的Excel
    # wb = copy(rb)  # 复制要写入数据的Excel
    # sheet = wb.get_sheet(0)  # 得到要写入数据的Excel的某一个表格
    #
    # for k in xrange(len(df2.ix[0,:])):
    #     if isinstance(df2.columns[k], np.int64) or isinstance(
    #             df2.columns[k], np.float64):  # 判断数字形式的
    #         # print type(data.ix[i, j])
    #         sheet.write(len(df1) + 1, k, float(df2.columns[k]))
    #     elif isinstance(df2.columns[k], unicode):  # 判断是否是 unicode 类型
    #         sheet.write(len(df1)+1, k, df2.columns[k])
    #     else:
    #         print type(df2.columns[k])
    #         sheet.write(len(df1) +1, k, df2.columns[k])
    #
    # for i in range(len(df2)):
    #     for j in xrange(len(df2.ix[0,:])):
    #
    #         if isinstance(df2.ix[i, j], np.int64) or isinstance(
    #                 df2.ix[i, j], np.float64):  # 判断数字形式的
    #             print type(df2.ix[i, 0])
    #             sheet.write(len(df1)+i+2,j, float(df2.ix[i, j]))
    #         elif isinstance(df2.ix[i, j], unicode):  # 判断是否是 unicode 类型
    #             print type(df2.ix[i, j]),'////////////////////'
    #             sheet.write(len(df1)+i+2,j, df2.ix[i, j])
    #         else:
    #             print type(df2.ix[i, j]),'#############'
    #             sheet.write(len(df1)+i+2,j, df2.ix[i, j])

    # for i in range(len(df2)):
    #     for j in xrange(len(df2.ix[0,:])):
    #         if isinstance(df2.ix[i, j], np.int64) or isinstance(
    #                 df2.ix[i, j], np.float64):  # 判断数字形式的
    #             # print type(data.ix[i, j])
    #             sheet.write(len(df1)+i+1,j, float(df2.ix[i, j]))
    #         elif isinstance(df2.ix[i, j], unicode):  # 判断是否是 unicode 类型
    #             # print type(data.ix[i, j])
    #             sheet.write(len(df1)+i+1,j, df2.ix[i, j])
    #         else:
    #             print type(df2.ix[i, j])
    #             sheet.write(len(df1)+i+1,j, unicode(df2.ix[i, j], "utf-8"))

    # wb.save(u'G:\\zlw_paper_new\\train_air\\excel\\{0}to{1}.xls'.format(o1, d1))
    # print type(df2.ix[0, 0])

if __name__=='__main__':

    od_data = pd.read_excel(u'G:\\zlw_paper_new\\train_air\\ODAIR.xlsx')
    for data in od_data.values:
        data_arrange(data[0], data[1])
    # data_arrange(u'北京', u'西安')



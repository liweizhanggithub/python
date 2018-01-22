# -*- coding: utf-8 -*-
"""
连接数据库，
进行不同OD的列车停站方案数据提取,sql语句是 a_sql.py 中的a_sql

"""
import numpy as np
import pandas as pd
import openpyxl as xls
import warnings     # python开发中经常遇到报错的情况，但是warning通常并不影响程序的运行，
warnings.filterwarnings("ignore")   # 这两句话就忽略了警告错误的输出
from openpyxl.writer.excel import ExcelWriter
import Connect_to_oracle_188.connect_oracle as oc
from a_sql import a_sql
import pickle as plk
from xlutils.copy import copy
from xlrd import open_workbook


def fangan(o1, d1):
    """
    连接数据库，获取OD 的列车停站方案数据
    :param o: O
    :param d: D
    :return:
    """
    oracle = oc.Oracle()

    df = oracle.query_data(a_sql % (o1, d1))

    # 将查询结果写入Excel里
    """
    创建workbook
    """
    filename = u'G:\\000-big papper\\2\\2.2\\列车停站方案\\%sto%s列车停站方案.xlsx' % (o1, d1)

    df.to_excel(filename, sheet_name=u'列车停站方案')
    oracle.close_oralce()

if __name__ == '__main__':
    od_data = pd.read_excel(u'G:\\zlw_paper_new\\OD.xlsx')
    for data in od_data.values:
        try:
            fangan(data[0],data[1])
        except BaseException:
            pass
    # fangan(u'北京',u'长沙')
# -*- coding: utf-8 -*-
"""
同一OD下将相同车次标相同数字，为画方案图准备数据
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

def train_biaohao(o1,d1):

    df=pd.read_excel(u'G:\\000-big papper\\2\\2.2\\列车停站方案\\%sto%s列车停站方案.xlsx'  % (o1, d1))
    df['NO']=0
    df = pd.DataFrame(df)

    df1=df.drop_duplicates(['TRAINNO'])  # 删除车次的重复项
    trainnumber=list(df1['TRAINNO'])


    for i in range(len(trainnumber)):
        for j in range(len(df)):
            if df['TRAINNO'][j]==trainnumber[i]:
                df['NO'][j]=i                # 当时就是因为df['NO'][j]=i 没有加j写成了df['NO']=i，调试了好长时间

    df = pd.DataFrame(df)

    filename = u'G:\\000-big papper\\2\\2.2\\列车停站方案\\列车停站方案标号\\%sto%s列车停站方案.xlsx' % (o1, d1)
    df.to_excel(filename, sheet_name=u'列车停站方案标号')

if __name__ == '__main__':
    od_data = pd.read_excel(u'G:\\zlw_paper_new\\OD.xlsx')
    for data in od_data.values:
        try:
            train_biaohao(data[0],data[1])
        except BaseException:
            pass






# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:31:17 2015

@author: wtl
"""
import cx_Oracle as cx  # 在系统中导入 cx_Oracle 包
import Oracle_user_info as oc  # 数据库连接，自己写的Oracle_user_info模块里面有要连接的数据库的信息
import os
import sys
import pandas as pd


class Oracle:
    def __init__(self):
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 获取出中文数据
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.dsn = cx.makedsn(oc.host, oc.port, oc.sid)  # cx.makedsn 返回一个用于进行数据库连接的dsn参数
        # cx.connect 用于创建与数据库的连接的构造函数，返回连接对象。
        self.con = cx.connect(oc.username, oc.password, self.dsn, encoding='utf-8')
        self.cursor = self.con.cursor()  # cursor 用于创建游标的构造函数，使用连接返回新的游标对象。

    def query_data(self, sql):         # 查询语句的方法
        columns = []
        self.cursor.execute(sql)       # 执行查询SQL
        index = self.cursor.description
        train_psg = self.cursor.fetchall()   # 获取返回结果
        for i in range(len(index)):
            columns.append(index[i][0])
        df = pd.DataFrame(train_psg, columns=columns)
        return df

    def close_oralce(self):         # 关闭数据库连接的方法
        self.cursor.close()      # 关闭连接，释放资源
        self.con.close()        # 关闭连接，释放资源


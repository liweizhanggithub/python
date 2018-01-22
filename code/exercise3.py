# -*- coding: utf-8 -*-
"""
利用python连接Oracle的类，来进行实例exercise1的操作
"""
import pandas as pd
import exercise2 as oc
from exercise4 import sql

oracle=oc.Oracle2()
df=oracle.query_data(sql)
print df

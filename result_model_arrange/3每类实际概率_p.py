# -*- coding: utf-8 -*-
"""
计算原始数据每类实际的概率，包括高铁概率、航空概率、每类高铁条件概率、每类航空条件概率、每类高铁概率、每类航空概率
"""
import pandas as pd
import numpy as np

def true_p(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    df=pd.read_csv(u'G:\\zlw_paper_new\\train_air\\excel_normal\\excel_normal_分类\\%sto%s.csv' % (o1,d1))
    df1=df[['code','TRAFFIC','PSGNUM']]

    df2=df1.groupby(['TRAFFIC']).sum()
    T_A=sum(df2['PSGNUM'])     ###### 选择高铁和航空人数之和 ######

    TRAIN_PSGNUM=df1[df1['TRAFFIC']=='train']['PSGNUM'].sum()    ### 选择高铁总人数 #####
    AIR_PSGNUM=df1[df1['TRAFFIC']=='air']['PSGNUM'].sum()         #### 选择航空总人数 ######

    every_TRAIN_PSGNUM=df1[df1['TRAFFIC']=='train'][['code','PSGNUM']].groupby([u'code']).sum()  ### 选择高铁的每类人数 #####
    every_AIR_PSGNUM=df1[df1['TRAFFIC']=='air'][['code','PSGNUM']].groupby([u'code']).sum()     ### 选择航空的每类人数 #####

    PTR=TRAIN_PSGNUM/T_A                          ###### 选择   高铁   概率 ######
    PAIR=AIR_PSGNUM/T_A                             ###### 选择   航空   概率 ######

    PtrainTR=every_TRAIN_PSGNUM/TRAIN_PSGNUM       ###### 选择  每类高铁  条件概率 ######
    PairAIR=every_AIR_PSGNUM/AIR_PSGNUM      ###### 选择  每类航空  条件概率 ######

    Ptrain=every_TRAIN_PSGNUM/T_A       ###### 选择  每类高铁  概率 ######
    Pair=every_AIR_PSGNUM/T_A      ###### 选择  每类航空  概率 ######

    df4=np.array(PTR).reshape(1,1)
    df5=pd.DataFrame(df4)

    df6=np.array(PAIR).reshape(1,1)
    df7=pd.DataFrame(df6)

    df3 = pd.concat([df5,df7,PtrainTR,Ptrain],axis=1)

    df3.rename(columns={0: 'TR',0: 'AIR',
                        'PSGNUM': 'trainTR', 'PSGNUM': 'train',
                       }, inplace=True)
    df33=pd.concat([df5,df7,PairAIR,Pair],axis=1)

    df33.rename(columns={0: 'TR', 0: 'AIR',
                        'PSGNUM': 'trainTR', 'PSGNUM': 'train',
                        }, inplace=True)

    df3.to_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\实际每类概率\\%sto%s_TRAIN_p.xlsx' % (o1,d1))
    df33.to_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\实际每类概率\\%sto%s_AIR_p.xlsx' % (o1,d1))

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        true_p(data[0], data[1])

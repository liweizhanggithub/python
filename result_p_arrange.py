# -*- coding: utf-8 -*-
"""
将每个OD下的每个车次及每个航班的概率连接起来，
然后将每个类别的高铁航空概率、条件概率、每类概率链接过来，为求得每类弹性值准备数据

"""
import pandas as pd

def result_p_arrange(o1,d1):
    """
    :param o1:
    :param d1:
    :return:
    """
    df1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_TRAIN.xls' % (o1,d1))
    # df1['TRAFFIC']='train'
    # df3=pd.DataFrame(df1)
    # df5=df3[['code','CHO','TRAFFIC','PTR.2','PAIR.2','PtrainTR.2','Ptrain.2']]
    # df5.rename(columns={'PTR.2':'PTR','PAIR.2':'PAIR','PtrainTR.2':'PtrainTR','Ptrain.2':'Ptrain'},inplace=True)
    # df5.sort_index(axis=0, ascending=True, by='CHO')
    df7 = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN.xlsx' % (o1, d1))
    df8 = df7[['code', 'TRAFFIC', 'PtrainTR_same_stage', 'Ptrain_same_stage']]
    # df9 = pd.merge(df5, df8, on=['code', 'TRAFFIC'])
    df9=pd.merge(df1,df8,on='code')
    df10=pd.DataFrame(df9)
    # df10.sort_index(axis=0, ascending=True, by='CHO')
    # df11=pd.DataFrame(df10)
    df10.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\TRAIN_p_new.csv' % (o1,d1),encoding = 'gbk')

    df12=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_AIR.xls' %(o1,d1))
    df13 = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_AIR.xlsx' % (o1, d1))
    df14 = df13[['code', 'TRAFFIC', 'PairAIR_same_stage', 'Pair_same_stage']]
    # df9 = pd.merge(df5, df8, on=['code', 'TRAFFIC'])
    df15 = pd.merge(df12, df14, on='code')
    # df16 = pd.DataFrame(df15)
    # df16.sort_index(axis=0, ascending=True, by='CHO')
    df17 = pd.DataFrame(df15)
    df17.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\AIR_p_new.csv' % (o1, d1), encoding='gbk')

    # df2['TRAFFIC']='air'
    # df4=pd.DataFrame(df2)
    # df6=df4[['code','CHO','TRAFFIC','PTR.2','PAIR.2','PairAIR.2','Pair.2']]
    # df6.rename(columns={'PTR.2':'PTR','PAIR.2':'PAIR','PairAIR.2':'PtrainTR','Pair.2':'Ptrain'},inplace=True)
    # df6.sort_index(axis=0, ascending=True, by='CHO')

    # df11 = pd.merge(df6, df8, on=['code', 'TRAFFIC'])
    # df12 = pd.DataFrame(df11)
    # # df12.sort_index(axis=0, ascending=True, by='CHO')
    # df12.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\AIR_p_new.csv' % (o1, d1),
    #             encoding='gbk')

    # df=pd.concat([df5,df6],axis=0)

    # df7=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN_AIR.xlsx' % (o1,d1))
    # df8=df7[['code','TRAFFIC','PtrainTR_same_stage','Ptrain_same_stage']]
    # df9=pd.merge(df,df8,on=['code','TRAFFIC'])

    # df10=pd.DataFrame(df9)
    # df10.to_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\%sto%s_TRAIN_AIR_p_new.csv' % (o1,d1,o1,d1),encoding = 'gbk')

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        result_p_arrange(data[0], data[1])
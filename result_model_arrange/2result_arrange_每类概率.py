# -*- coding: utf-8 -*-
"""
计算出 同时估计法、分阶段估计法、同时估计法与分阶段估计法相结合的方法、MNL 、 原始数据统计出来的、每一类产品的概率
最终的数据说明：高铁类别，
                同时估计法的选择高铁、选择航空、每一类高铁条件概率、每一类高铁概率；
                分阶段估计法的选择高铁、选择航空、每一类高铁条件概率、每一类高铁概率；
                同时与分阶段估计法的选择高铁、选择航空、每一类高铁条件概率、每一类高铁概率；
                MNL估计法的选择高铁、选择航空、每一类高铁条件概率、每一类高铁概率；
                原始数据统计出来的选择高铁、选择航空、每一类高铁条件概率、每一类高铁概率；
同理：          航空类别，
                同时估计法的选择高铁、选择航空、每一类航空条件概率、每一类航空概率；
                分阶段估计法的选择高铁、选择航空、每一类航空条件概率、每一类航空概率；
                同时与分阶段估计法的选择高铁、选择航空、每一类航空条件概率、每一类航空概率；
                MNL估计法的选择高铁、选择航空、每一类航空条件概率、每一类航空概率；
                原始数据统计出来的选择高铁、选择航空、每一类航空条件概率、每一类航空概率；

同时，将每一个OD的高铁与航空的数据写入到同一个文件中
但是，要注意，只有高铁与航空的数据的列名一样时，才会是我们想要的那种写入，因此对于df6.rename有两个版本，要注意独立执行，
在执行其中一种时，另一种要注释

即：分2步执行：首先注释掉##### 下面井号之间的是将高铁与航空分开的概率合并到一起 #########这块内容，将高铁数据与航空数据
分别写入到不同文件中；
然后解除上面注释，而是注释掉#######将航空数据独立写入到文件夹中，与下面的将高铁与航空分开的概率合并到一起 分开执行############
这块内容，这次是将高铁与航空数据合并写入到同一个文件中
"""
import pandas as pd

def result_arrange_p(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    ##### 高铁每类的数据概率#######
    df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_TRAIN.xls' % (o1,d1))
    df_1=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\实际每类概率\\%sto%s_TRAIN_p.xlsx' % (o1,d1))

    df2=df[['code','PtrainTR','Ptrain','PtrainTR.1','Ptrain.1',
            'PtrainTR.2','Ptrain.2','PtrainTR.3','Ptrain.3']].groupby([u'code']).sum()

    # df2['PTR_same']="%.2f%%" % (df['PTR'][1]*100)
    df2['PTR_same'] = df['PTR'][1]
    df2['PAIR_same']=df['PAIR'][1]

    df2['PTR_stage']=df['PTR.1'][1]
    df2['PAIR_stage']=df['PAIR.1'][1]

    df2['PTR_same_stage']=df['PTR.2'][1]
    df2['PAIR_same_stage']=df['PAIR.2'][1]

    df2['PTR_MNL']=df['PTR.3'][1]
    df2['PAIR_MNL']=df['PAIR.3'][1]

    df2['TR'] = df_1['AIR'][0]           #### 实际数据选择高铁概率
    df2['AIR'] = df_1['AIR.1'][0]        ######实际数据选择航空概率

    df2['trainTR']=df_1['train'][1:]       #####实际数据选择每一类高铁的条件概率
    df2['train'] = df_1['train.1'][1:]     #####实际数据选择每一类高铁的概率

    df2['TRAFFIC']='train'

    df3=pd.DataFrame(df2,columns=['TRAFFIC','PTR_same','PAIR_same','PtrainTR','Ptrain',
                                  'PTR_stage','PAIR_stage','PtrainTR.1','Ptrain.1',
                                  'PTR_same_stage','PAIR_same_stage','PtrainTR.2','Ptrain.2',
                                  'PTR_MNL','PAIR_MNL','PtrainTR.3','Ptrain.3',
                                  'TR','AIR','trainTR','train'])

    df3.rename(columns={'PtrainTR':'PtrainTR_same','Ptrain':'Ptrain_same',
                        'PtrainTR.1':'PtrainTR_stage', 'Ptrain.1':'Ptrain_stage',
                        'PtrainTR.2':'PtrainTR_same_stage', 'Ptrain.2':'Ptrain_same_stage',
                        'PtrainTR.3':'PtrainTR_MNL', 'Ptrain.3':'Ptrain_MNL',
                        'TR':'PTR_p', 'AIR':'PAIR_p',
                        'trainTR':'PtrainTR_p', 'train':'Ptrain_p'},inplace=True)
    df3.to_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN.xlsx' % (o1,d1))

    ##### 航空每类的数据概率#######
    df4=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_AIR.xls' % (o1,d1))
    df_2 = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new_每类概率\\实际每类概率\\%sto%s_AIR_p.xlsx' % (o1, d1))

    df5=df4[['code','PairAIR','Pair','PairAIR.1','Pair.1',
             'PairAIR.2','Pair.2','PairAIR.3','Pair.3']].groupby([u'code']).sum()

    df5['PTR_same']=df4['PTR'][1]
    df5['PAIR_same']=df4['PAIR'][1]

    df5['PTR_stage']=df4['PTR.1'][1]
    df5['PAIR_stage']=df4['PAIR.1'][1]

    df5['PTR_same_stage']=df4['PTR.2'][1]
    df5['PAIR_same_stage']=df4['PAIR.2'][1]

    df5['PTR_MNL']=df4['PTR.3'][1]
    df5['PAIR_MNL']=df4['PAIR.3'][1]

    df5['TR'] = df_2['AIR'][0]         #### 实际数据选择高铁概率
    df5['AIR'] = df_2['AIR.1'][0]       ######实际数据选择航空概率

    df5['airAIR']=df_2['train'][1:]       #####实际数据选择每一类航班的条件概率
    df5['air'] = df_2['train.1'][1:]       #####实际数据选择每一类航班的概率

    df5['TRAFFIC']='air'

    df6=pd.DataFrame(df5,columns=['TRAFFIC','PTR_same','PAIR_same','PairAIR','Pair',
                                  'PTR_stage','PAIR_stage','PairAIR.1','Pair.1',
                                  'PTR_same_stage','PAIR_same_stage','PairAIR.2','Pair.2',
                                  'PTR_MNL','PAIR_MNL','PairAIR.3','Pair.3','TR','AIR','airAIR','air'])

    ######将航空数据独立写入到文件夹中，与下面的将高铁与航空分开的概率合并到一起 分开执行############
    # df6.rename(columns={'PairAIR':'PairAIR_same','Pair':'Pair_same',
    #                     'PairAIR.1':'PairAIR_stage', 'Pair.1':'Pair_stage',
    #                     'PairAIR.2':'PairAIR_same_stage', 'Pair.2':'Pair_same_stage',
    #                     'PairAIR.3':'PairAIR_MNL', 'Pair.3':'Pair_MNL',
    #                     'TR':'PTR_p','AIR':'PAIR_p',
    #                     'airAIR':'PairAIR_p','air':'Pair_p'},inplace=True)
    # df6.to_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_AIR.xlsx' % (o1, d1))
    ######将航空数据独立写入到文件夹中，与下面的将高铁与航空分开的概率合并到一起 分开执行############

    ##### 下面井号之间的是将高铁与航空分开的概率合并到一起 #########
    df6.rename(columns={'PairAIR':'PtrainTR_same','Pair':'Ptrain_same',
                        'PairAIR.1':'PtrainTR_stage', 'Pair.1':'Ptrain_stage',
                        'PairAIR.2':'PtrainTR_same_stage', 'Pair.2':'Ptrain_same_stage',
                        'PairAIR.3':'PtrainTR_MNL', 'Pair.3':'Ptrain_MNL',
                        'TR':'PTR_p','AIR':'PAIR_p',
                        'airAIR':'PtrainTR_p','air':'Ptrain_p'},inplace=True)
    df7=pd.concat([df3,df6],axis=0)
    df8=pd.DataFrame(df7)
    df8.to_excel(u'G:\\000bigpaper\R程序整理\\result_arrange_new_new_每类概率\\%sto%s_TRAIN_AIR.xlsx' % (o1, d1))
    ##### 和上面井号相对应，是将高铁与航空分开的概率合并到一起 #########

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        result_arrange_p(data[0], data[1])

# -*- coding: utf-8 -*-
"""
将1.R、stage_solve1.R 以及 MNL-2.R 的程序
即将同时估计法、分阶段估计法、同时估计法与分阶段估计法相结合的方法、MNL模型的求解结果整合在一起
按照TRAIN、AIR分为两个文件夹，分别整合选择高铁的概率、选择航空的概率、条件概率、选择车次（航班）概率

"""
import pandas as pd

def result_arrange(o1,d1):
    """
    :param o1:
    :param d1:
    :return:
    """
    df1 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\TRAIN_result_1.csv' % (o1,d1))
    df2 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\TRAIN_result_stage.csv'% (o1,d1))
    df3 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\TRAIN_result_same2_stage1.csv'% (o1,d1))
    df4 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\TRAIN_result_MNL.csv'% (o1,d1))

    df5 = pd.concat([df1[['PTR', 'PAIR', 'PtrainTR', 'Ptrain']], df2[['PTR', 'PAIR', 'PtrainTR', 'Ptrain']],
                     df3[['PTR', 'PAIR', 'PtrainTR', 'Ptrain']], df4[['PTR', 'PAIR', 'PtrainTR', 'Ptrain']]], axis=1)

    alldata1 = pd.DataFrame(df5)
    alldata1.to_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_TRAIN.xls'% (o1,d1), index=False)

    df6 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\AIR_result_1.csv'% (o1,d1))
    df7 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\AIR_result_stage.csv'% (o1,d1))
    df8 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\AIR_result_same2_stage1.csv'% (o1,d1))
    df9 = pd.read_csv(u'G:\\000bigpaper\\R程序整理\\result_new_new\\%sto%s\\AIR_result_MNL.csv'% (o1,d1))

    df10 = pd.concat([df6[['PTR', 'PAIR', 'PairAIR', 'Pair']], df7[['PTR', 'PAIR', 'PairAIR', 'Pair']],
                      df8[['PTR', 'PAIR', 'PairAIR', 'Pair']], df9[['PTR', 'PAIR', 'PairAIR', 'Pair']]], axis=1)

    alldata2 = pd.DataFrame(df10)
    alldata2.to_excel(u'G:\\000bigpaper\\R程序整理\\result_arrange_new_new\\%sto%s_AIR.xls'% (o1,d1), index=False)


if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        result_arrange(data[0], data[1])

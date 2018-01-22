# -*- coding: utf-8 -*-
"""
1、将每类车次和航班所属类别链接过来，
2、然后将弹性值按照类别进行汇总合并

"""
import pandas as pd

def elastic_arrange_new(o1,d1):
    """

    :param o1:
    :param d1:
    :return:
    """
    df=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\分类匹配_T_A.xlsx',sheetname=u'%sto%s_T' % (o1,d1))
    df1=pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\Elastic_train_new.csv' % (o1,d1))
    df1['code']=df['code']
    df2 = df1.groupby([u'code']).mean()
    df3 = pd.DataFrame(df2)


    df4=pd.read_excel(u'G:\\000bigpaper\\R程序整理\\分类匹配_T_A.xlsx',sheetname=u'%sto%s_A' % (o1,d1))
    df5=pd.read_csv(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new\\%sto%s\\Elastic_air_new.csv' % (o1,d1))
    df5['code']=df4['code']
    df6 = df5.groupby([u'code']).mean()
    df7 = pd.DataFrame(df6)

    df7.rename(columns={'E_hdd_ont0_air':'E_hdd_ont0_train','E_hdd_ont1_air':'E_hdd_ont1_train','E_hdd_ont2_air':'E_hdd_ont2_train',
                        'E_hdd_offt0_air':'E_hdd_offt0_train','E_hdd_offt1_air':'E_hdd_offt1_train','E_hdd_offt2_air':'E_hdd_offt2_train',
                        'E_hdd_time_air':'E_hdd_time_train','E_hdd_sat_air':'E_hdd_sat_train','E_hdd_price_air':'E_hdd_price_train',
                        'E_hdd_stop_air':'E_hdd_stop_train','E_hdd_zhun_air':'E_hdd_zhun_train','E_hdd_cap_air':'E_hdd_cap_train',

                        'E_huu_conv_air':'E_huu_conv_train','E_huu_saf_air':'E_huu_saf_train',

                        'E_ydu_ont0_air':'E_ydu_ont0_train','E_ydu_ont1_air':'E_ydu_ont1_train','E_ydu_ont2_air':'E_ydu_ont2_train',
                        'E_ydu_offt0_air':'E_ydu_offt0_train','E_ydu_offt1_air':'E_ydu_offt1_train','E_ydu_offt2_air':'E_ydu_offt2_train',
                        'E_ydu_time_air':'E_ydu_time_train','E_ydu_sat_air':'E_ydu_sat_train','E_ydu_price_air':'E_ydu_price_train',
                        'E_ydu_stop_air':'E_ydu_stop_train','E_ydu_zhun_air':'E_ydu_zhun_train','E_ydu_cap_air':'E_ydu_cap_train',

                        'E_yud_conv_air':'E_yud_conv_train','E_yud_saf_air':'E_yud_saf_train',

                        'EC_hdd_ont0_air':'EC_hdd_ont0_train','EC_hdd_ont1_air':'EC_hdd_ont1_train','EC_hdd_ont2_air':'EC_hdd_ont2_train',
                        'EC_hdd_offt0_air':'EC_hdd_offt0_train','EC_hdd_offt1_air':'EC_hdd_offt1_train','EC_hdd_offt2_air':'EC_hdd_offt2_train',
                        'EC_hdd_time_air':'EC_hdd_time_train','EC_hdd_sat_air':'EC_hdd_sat_train','EC_hdd_price_air':'EC_hdd_price_train',
                        'EC_hdd_stop_air':'EC_hdd_stop_train','EC_hdd_zhun_air':'EC_hdd_zhun_train','EC_hdd_cap_air':'EC_hdd_cap_train',

                        'EC_huu_conv_air':'EC_huu_conv_train','EC_huu_saf_air':'EC_huu_saf_train',

                        'EC_ydu_ont0_air':'EC_ydu_ont0_train','EC_ydu_ont1_air':'EC_ydu_ont1_train','EC_ydu_ont2_air':'EC_ydu_ont2_train',
                        'EC_ydu_offt0_air':'EC_ydu_offt0_train','EC_ydu_offt1_air':'EC_ydu_offt1_train','EC_ydu_offt2_air':'EC_ydu_offt2_train',
                        'EC_ydu_time_air':'EC_ydu_time_train','EC_ydu_sat_air':'EC_ydu_sat_train','EC_ydu_price_air':'EC_ydu_price_train',
                        'EC_ydu_stop_air':'EC_ydu_stop_train','EC_ydu_zhun_air':'EC_ydu_zhun_train','EC_ydu_cap_air':'EC_ydu_cap_train',

                        'EC_yud_conv_air':'EC_yud_conv_train','EC_yud_saf_air':'EC_yud_saf_train'},inplace=True)

    df8=pd.concat([df3,df7],axis=0)
    df9=pd.DataFrame(df8,columns=[
                                  'E_hdd_ont0_train','E_hdd_ont1_train','E_hdd_ont2_train',
                                  'E_hdd_offt0_train','E_hdd_offt1_train','E_hdd_offt2_train',
                                  'E_hdd_time_train','E_hdd_sat_train','E_hdd_price_train',
                                  'E_hdd_stop_train','E_hdd_zhun_train','E_ydu_cap_train',

                                  'E_huu_conv_train','E_huu_saf_train',

                                  'E_ydu_ont0_train','E_ydu_ont1_train','E_ydu_ont2_train',
                                  'E_ydu_offt0_train','E_ydu_offt1_train','E_ydu_offt2_train',
                                  'E_ydu_time_train','E_ydu_sat_train','E_ydu_price_train',
                                  'E_ydu_stop_train','E_ydu_zhun_train','E_ydu_cap_train',

                                  'E_yud_conv_train','E_yud_saf_train',

                                  'EC_hdd_ont0_train', 'EC_hdd_ont1_train', 'EC_hdd_ont2_train',
                                  'EC_hdd_offt0_train', 'EC_hdd_offt1_train', 'EC_hdd_offt2_train',
                                  'EC_hdd_time_train', 'EC_hdd_sat_train', 'EC_hdd_price_train',
                                  'EC_hdd_stop_train', 'EC_hdd_zhun_train', 'EC_ydu_cap_train',

                                  'EC_huu_conv_train', 'EC_huu_saf_train',

                                  'EC_ydu_ont0_train', 'EC_ydu_ont1_train', 'EC_ydu_ont2_train',
                                  'EC_ydu_offt0_train', 'EC_ydu_offt1_train', 'EC_ydu_offt2_train',
                                  'EC_ydu_time_train', 'EC_ydu_sat_train', 'EC_ydu_price_train',
                                  'EC_ydu_stop_train', 'EC_ydu_zhun_train', 'EC_ydu_cap_train',

                                  'EC_yud_conv_train', 'EC_yud_saf_train'
                                  ])
    df9.to_excel(u'G:\\000bigpaper\\R程序整理\\Elastic_3plot_new_每类弹性\\%sto%s_Elastic_train_air_new.xlsx' % (o1,d1))

if __name__ == '__main__':
    od = pd.read_excel(u'G:\\000bigpaper\\R程序整理\\od.xlsx')
    for data in od.values:
        elastic_arrange_new(data[0], data[1])

# -*- coding: utf-8 -*-
"""
a_sql取出特定OD下的列车时刻表，包括车次、停站顺序、停站名
"""
a_sql='select distinct t.trainno,t.stationorder,t.stopsta ' \
      'from timetable_zlw t ' \
      'where t.trainno in ' \
      '(select distinct a.trainno from data_zlw a where substr(a.trainno, 0, 1) in ('"'G'"','"'D'"') ' \
      'and substr(a.onstation,0,2) = '"'%s'"' and substr(a.offstation,0,2) = '"'%s'"') ' \
      'order by t.trainno,t.stationorder asc'
print a_sql

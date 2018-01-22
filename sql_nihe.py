# -*- coding: utf-8 -*-

sql_nihe_wu='select distinct t.onstation,t.offstation,t.trainno,' \
            'to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') as ontime,' \
            'to_char(to_date(to_char(t.offtime),'"'hh24:mi'"'),'"'hh24:mi'"') as offtime,' \
            'b.price as price,t.seat_num,' \
            'c.kezuolv as kezuolv from air_seatnum t ' \
            'left join ' \
            '(select distinct  a.onstation,a.offstation,a.trainno,' \
            'round(sum(a.price) over (partition by a.onstation,a.offstation,a.trainno)/count(a.boarddate)' \
            'over (partition by a.onstation,a.offstation,a.trainno)) as price ' \
            'from ' \
            '(select distinct k.onstation,k.offstation,k.boarddate,k.trainno,' \
            'sum(k.price) over (partition by k.onstation,k.offstation,k.trainno,k.boarddate)/count(k.bookdate)' \
            'over (partition by k.onstation,k.offstation,k.trainno,k.boarddate) as price from air_price k)a) b ' \
            'on (b.onstation=t.onstation and b.offstation=t.offstation and b.trainno=t.trainno) ' \
            'left join ' \
            '(select distinct h.trainno,h.onstation,h.offstation,' \
            'round(sum(h.kezuolv) over (partition by h.trainno,h.onstation,h.offstation)/count(h.boarddate) ' \
            'over (partition by h.trainno,h.onstation,h.offstation),4) as kezuolv from air_kezuolv h) c ' \
            'on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno) ' \
            'where t.boarddate='"'20170315'"' ' \
            'and substr(t.onstation,0,2)= '"'%s'"' and substr(t.offstation,0,2)= '"'%s'"' ' \
            'order by to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') asc'

sql_nihe_you='select distinct t.onstation,t.offstation,t.trainno,' \
             'to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') as ontime,' \
             'to_char(to_date(to_char(t.offtime),'"'hh24:mi'"'),'"'hh24:mi'"') as offtime,' \
             'b.price as price,t.seat_num,' \
             'c.kezuolv as kezuolv from air_seatnum t ' \
             'left join ' \
             '(select distinct  a.onstation,a.offstation,a.trainno,round(sum(a.price) ' \
             'over (partition by a.onstation,a.offstation,a.trainno)/count(a.boarddate)' \
             'over (partition by a.onstation,a.offstation,a.trainno)) as price ' \
             'from ' \
             '(select distinct k.onstation,k.offstation,k.boarddate,k.trainno,' \
             'sum(k.price) over (partition by k.onstation,k.offstation,k.trainno,k.boarddate)/count(k.bookdate)' \
             'over (partition by k.onstation,k.offstation,k.trainno,k.boarddate) as price from air_price k )a) b ' \
             'on (b.onstation=t.onstation and b.offstation=t.offstation and b.trainno=t.trainno) ' \
             'left join ' \
             '(select distinct h.trainno,h.onstation,h.offstation,' \
             'round(sum(h.kezuolv) over (partition by h.trainno,h.onstation,h.offstation)/count(h.boarddate) ' \
             'over (partition by h.trainno,h.onstation,h.offstation),4) as kezuolv ' \
             'from air_kezuolv h where h.boarddate not in ('"'20170315'"')) c ' \
             'on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno) ' \
             'where t.boarddate='"'20170315'"' ' \
             'and substr(t.onstation,0,2)= '"'%s'"' and substr(t.offstation,0,2)= '"'%s'"' ' \
             'order by to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') asc'

sql_0315='select distinct t.onstation,t.offstation,t.trainno,t.boarddate,' \
         'to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') as ontime,' \
         'to_char(to_date(to_char(t.offtime),'"'hh24:mi'"'),'"'hh24:mi'"') as offtime,' \
         'round(c.kezuolv,4) as  kezuolv ' \
         'from air_seatnum t ' \
         'left join air_kezuolv c ' \
         'on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno and t.boarddate=c.boarddate) ' \
         'where t.boarddate='"'20170315'"' and substr(t.onstation,0,2)= '"'%s'"' ' \
         'and substr(t.offstation,0,2)= '"'%s'"' ' \
         'order by to_char(to_date(to_char(t.ontime),'"'hh24:mi'"'),'"'hh24:mi'"') asc'
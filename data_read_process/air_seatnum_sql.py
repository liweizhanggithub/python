# -*- coding: utf-8 -*-
air_seatnum_sql_yiqian='select distinct t.onstation,t.offstation,t.trainno,t.ontime,t.offtime, ' \
                'abs((to_date(t.offtime,'"'hh24:mi'"') -to_date(t.ontime,'"'hh24:mi'"')) * 24 * 60) as traintime,' \
                'b.price as price,g.stopnum as stopnum,g.timerate as timerate,' \
                't.seat_num,c.kezuolv as kezuolv,g.mile as mile from air_seatnum t ' \
                'left join ' \
                '(select distinct  a.onstation,a.offstation,a.trainno,' \
                'round(sum(a.price) over (partition by a.onstation,a.offstation,a.trainno)/count(a.boarddate)' \
                'over (partition by a.onstation,a.offstation,a.trainno)) as price ' \
                'from (select distinct k.onstation,k.offstation,k.boarddate,k.trainno,' \
                'sum(k.price) over (partition by k.onstation,k.offstation,k.trainno,k.boarddate)/count(k.bookdate) ' \
                'over (partition by k.onstation,k.offstation,k.trainno,k.boarddate) as price from air_price k)a) b ' \
                'on (b.onstation=t.onstation and b.offstation=t.offstation and b.trainno=t.trainno) ' \
                'left join' \
                ' (select distinct h.trainno,h.onstation,h.offstation,round(sum(h.kezuolv)' \
                ' over (partition by h.trainno,h.onstation,h.offstation)/count(h.boarddate) ' \
                'over (partition by h.trainno,h.onstation,h.offstation),2) as kezuolv from air_kezuolv h) c ' \
                'on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno) ' \
                'left join ' \
                'air_zhundianlv g on (g.onstation=t.onstation and g.offstation=t.offstation and g.trainno=t.trainno) ' \
                'where t.boarddate=20170315 and t.onstation like '"'%s'"' and t.offstation like '"'%s'"' ' \
                'order by t.ontime asc'

air_seatnum_sql1='select distinct p.trainno,p.onstation,p.offstation,p.traffic,p.safety,p.convience,p.mile,' \
                'p.ontime,p.offtime,' \
                '(case when p.traintime<500 then p.traintime else (1440-p.traintime) end) as traintime,' \
                'p.price,p.seattype,p.stopnum,p.timerate,' \
                'p.seat_num,p.kezuolv ' \
                'from ' \
                '(select distinct t.trainno,t.onstation,t.offstation,' \
                '(case when substr(t.trainno,0,1) not in ('"'航空'"') then '"'air'"' else '"'train'"' end) ' \
                'as traffic,m.safety_air as safety,m.con_air as convience,g.mile as mile, t.ontime,t.offtime,' \
                'abs((to_date(t.offtime,'"'hh24:mi'"') -to_date(t.ontime,'"'hh24:mi'"')) * 24 * 60) as traintime,' \
                'b.price as price,' \
                '(case when substr(t.trainno,0,2) not in ('"'航'"') then '"'经济舱'"' else '"'航空'"' end) ' \
                'as seattype,g.stopnum as stopnum,g.timerate as timerate,t.seat_num,c.kezuolv as kezuolv ' \
                'from ' \
                'air_seatnum t ' \
                'left join ' \
                '(select distinct  a.onstation,a.offstation,a.trainno, ' \
                'round(sum(a.price) over (partition by a.onstation,a.offstation,a.trainno)/count(a.boarddate)' \
                'over (partition by a.onstation,a.offstation,a.trainno)) as price ' \
                'from ' \
                '(select distinct k.onstation,k.offstation,k.boarddate,k.trainno, ' \
                'sum(k.price) over (partition by k.onstation,k.offstation,k.trainno,k.boarddate)/count(k.bookdate)' \
                'over (partition by k.onstation,k.offstation,k.trainno,k.boarddate) as price ' \
                'from ' \
                'air_price k)a) b on (b.onstation=t.onstation and b.offstation=t.offstation and b.trainno=t.trainno) ' \
                'left join (select distinct h.trainno,h.onstation,h.offstation, ' \
                'round(sum(h.kezuolv) over (partition by h.trainno,h.onstation,h.offstation)/count(h.boarddate) ' \
                'over (partition by h.trainno,h.onstation,h.offstation),2) as kezuolv ' \
                'from ' \
                'air_kezuolv h) c on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno) ' \
                'left join air_zhundianlv g on (g.onstation=t.onstation and g.offstation=t.offstation ' \
                'and g.trainno=t.trainno) ' \
                'left join air_safety m on (m.onstation=substr(t.onstation,0,2) ' \
                'and m.offstation=substr(t.offstation,0,2)) ' \
                'where t.boarddate=20170315 ' \
                'and substr(t.onstation,0,2) = '"'%s'"' and substr(t.offstation,0,2) ='"'%s'"')p ' \
                'order by p.ontime asc'

air_seatnum_sql='select distinct to_char(p.trainno) as cho,to_char(p.onstation) as onstation,p.offstation,p.traffic,' \
                'p.safety,p.convience,p.mile,' \
                'case when (to_number(substr(p.ontime, 0, 2)) between 6 and 11) then 1 else 0 end as ontime0,' \
                'case when (to_number(substr(p.ontime, 0, 2)) between 12 and 17) then 1 else 0 end as ontime1,' \
                'case when (to_number(substr(p.ontime, 0, 2)) between 18 and 20) then 1 else 0 end as ontime2,' \
                'case when (to_number(substr(p.ontime, 0, 2)) between 21 and 24) then 1 else 0 end as ontime3,' \
                'case when (to_number(substr(p.offtime, 0, 2)) between 6 and 11) then 1 else 0 end as offtime0,' \
                'case when (to_number(substr(p.offtime, 0, 2)) between 12 and 17) then 1 else 0 end as offtime1,' \
                'case when (to_number(substr(p.offtime, 0, 2)) between 18 and 20) then 1 else 0 end as offtime2,' \
                'case when (to_number(substr(p.offtime, 0, 2)) between 21 and 24) then 1 else 0 end as offtime3,' \
                '(case when p.traintime<500 then p.traintime else (1440-p.traintime) end) as traintime,' \
                'p.price,' \
                'case when (p.seattype ='"'高级动卧'"' or p.seattype ='"'动卧'"' or p.seattype ='"'软卧'"') then 4 ' \
                'when p.seattype ='"'商务座'"' or p.seattype ='"'特等座'"' then 3 ' \
                'when (p.seattype ='"'一等座'"' or p.seattype ='"'经济舱'"') then 2 ' \
                'else 1 end as seattype,' \
                'p.stopnum,(p.timerate) as zhundianlv,(p.seat_num) as seat_capacity,' \
                '(p.kezuolv) as psgnum ' \
                'from ' \
                '(select distinct t.trainno,t.onstation,t.offstation,' \
                '(case when substr(t.trainno,0,1) not in ('"'航空'"') then '"'air'"' else '"'train'"' end) ' \
                'as traffic,m.safety_air as safety,m.con_air as convience,g.mile as mile,t.ontime,t.offtime,' \
                'abs((to_date(t.offtime,'"'hh24:mi'"') -to_date(t.ontime,'"'hh24:mi'"')) * 24 * 60) as traintime,' \
                'b.price as price,' \
                '(case when substr(t.trainno,0,2) not in ('"'航'"') then '"'经济舱'"' else '"'航空'"' end) ' \
                'as seattype,g.stopnum as stopnum,g.timerate as timerate,t.seat_num,c.kezuolv as kezuolv ' \
                'from ' \
                'air_seatnum t ' \
                'left join (select distinct  a.onstation,a.offstation,a.trainno,' \
                'round(sum(a.price) over (partition by a.onstation,a.offstation,a.trainno)/count(a.boarddate)' \
                'over (partition by a.onstation,a.offstation,a.trainno)) as price ' \
                'from (select distinct k.onstation,k.offstation,k.boarddate,k.trainno, ' \
                'sum(k.price) over (partition by k.onstation,k.offstation,k.trainno,k.boarddate)/count(k.bookdate)over' \
                '(partition by k.onstation,k.offstation,k.trainno,k.boarddate) as price ' \
                'from ' \
                'air_price k)a) b on (b.onstation=t.onstation and b.offstation=t.offstation and b.trainno=t.trainno) ' \
                'left join (select distinct h.trainno,h.onstation,h.offstation,' \
                'round(sum(h.kezuolv) over (partition by h.trainno,h.onstation,h.offstation)/count(h.boarddate) over ' \
                '(partition by h.trainno,h.onstation,h.offstation),2) as kezuolv from air_kezuolv h) c ' \
                'on (c.onstation=t.onstation and c.offstation=t.offstation and c.trainno=t.trainno) ' \
                'left join air_zhundianlv g ' \
                'on (g.onstation=t.onstation and g.offstation=t.offstation and g.trainno=t.trainno) ' \
                'left join air_safety m ' \
                'on (m.onstation=substr(t.onstation,0,2) and m.offstation=substr(t.offstation,0,2)) ' \
                'where t.boarddate='"'20170315'"' ' \
                'and substr(t.onstation,0,2)= '"'%s'"' and substr(t.offstation,0,2)= '"'%s'"')p ' \
                'order by to_char(p.trainno) asc'

 # 当时20170315没有加引号引起来，找了一晚上错误在哪里也没找到，大早上一来就找到了，要谨记
 #当时case when 中时，每一个when后面没有逗号，记住没有逗号
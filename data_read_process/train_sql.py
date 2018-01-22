# -*- coding: utf-8  -*-
train_sql='select distinct r.cho,r.onstation,r.offstation,r.traffic,r.safety,r.convience,r.mile,' \
          'case when (to_number(substr(r.ontime, 0, 2)) between 6 and 11) then 1 else 0 end as ontime0,' \
          'case when (to_number(substr(r.ontime, 0, 2)) between 12 and 17) then 1 else 0 end as ontime1,' \
          'case when (to_number(substr(r.ontime, 0, 2)) between 18 and 20) then 1 else 0 end as ontime2,' \
          'case when (to_number(substr(r.ontime, 0, 2)) between 21 and 24) then 1 else 0 end as ontime3,' \
          'case when (to_number(substr(r.offtime, 0, 2)) between 6 and 11) then 1 else 0 end as offtime0,' \
          'case when (to_number(substr(r.offtime, 0, 2)) between 12 and 17) then 1 else 0 end as offtime1,' \
          'case when (to_number(substr(r.offtime, 0, 2)) between 18 and 20) then 1 else 0 end as offtime2,' \
          'case when (to_number(substr(r.offtime, 0, 2)) between 21 and 24) then 1 else 0 end as offtime3,' \
          'r.traintime,r.price,' \
          'case ' \
          'when (r.seattype ='"'高级动卧'"' or r.seattype ='"'动卧'"' or r.seattype ='"'软卧'"') then 4 ' \
          'when r.seattype ='"'商务座'"' or r.seattype ='"'特等座'"' then 3 ' \
          'when (r.seattype ='"'一等座'"' or r.seattype ='"'经济舱'"') then 2 else 1 end as seattype,' \
          'r.stopnum,r.zhundianlv,r.seat_capacity,' \
          'sum(r.psgnum) over (partition by r.cho) as psgnum ' \
          'from ' \
          '(select distinct  e.trainno || e.seattype as cho,e.onstation,e.offstation,' \
          '(case when substr(e.trainno,0,1) in ('"'G'"','"'D'"') then '"'train'"' else '"'air'"' end)' \
          ' as traffic,m.safety_train as safety,m.con_train as convience,' \
          'max(e.mile) over (partition by e.trainno,e.onstation,e.offstation) as mile,' \
          'e.ontime,' \
          'max(e.offtime) over (partition by (e.trainno || e.seattype)) as offtime,' \
          'max(e.traintime) over (partition by e.trainno,e.onstation,e.offstation) as traintime,' \
          'max(e.price) over (partition by e.seattype) as price,e.seattype,' \
          'max(abs(e.d_staorder-e.o_staorder)-1) over (partition by e.trainno) as stopnum,' \
          '(case when substr(e.trainno,0,1) in ('"'G'"','"'D'"') then '"'1.00'"' else '"'nan'"' end) ' \
          'as zhundianlv,e.seat_capacity,round(sum(e.psgnum) over ' \
          '(partition by e.onstation,e.offstation,e.trainno,e.seattype)/count(distinct e.boarddate) ' \
          'over (partition by e.onstation,e.offstation,e.trainno,e.seattype)) as psgnum ' \
          'from ' \
          '(select distinct t.boarddate,t.trainno,' \
          'substr(t.onstation,0,2) as onstation,substr(t.offstation,0,2) as offstation,t.ontime,t.offtime,' \
          'abs((to_date(t.offtime,'"'hh24:mi'"') -to_date(t.ontime,'"'hh24:mi'"')) * 24 * 60) as traintime,' \
          't.income/t.psgnum as price,t.seattype,t.tickettype,t.psgnum,a.stationorder as o_staorder, ' \
          'b.stationorder as d_staorder,f.seat_capacity as seat_capacity,t.mile from data_zlw t ' \
          'left join timetable_zlw a on (a.trainno =t.trainno and a.stopsta =t.onstation) ' \
          'left join timetable_zlw b on (b.trainno =t.trainno and b.stopsta =t.offstation) ' \
          'left join seat_trainno_capacity f on(f.trainno=t.trainno and f.seattype=t.seattype) ' \
          'where substr(t.onstation,0,2) = '"'%s'"' and substr(t.offstation,0,2) = '"'%s'"'and substr(t.trainno, 0, 1) ' \
          'in ('"'G'"', '"'D'"'))e ' \
          'left join air_safety m ' \
          'on (m.onstation=substr(e.onstation,0,2) and m.offstation=substr(e.offstation,0,2)))r order by r.cho asc'

print train_sql

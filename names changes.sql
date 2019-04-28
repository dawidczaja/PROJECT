#alter table chapter_73 modify HTS_code text;
#alter table chapter_73 add Title text;
alter table chapter_73 change lft left_mark int(10);
alter table chapter_73 change rght right_mark int(10);
#alter table section_xv rename as Section_XV;
#delete from section_xv;
#drop table chapter_73;
#describe Section_xv;
update chapter_73
set hts_code = '7307.29.8090' where id = 51;
select * from chapter_73;



























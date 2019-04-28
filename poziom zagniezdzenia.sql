#select count(id) as depth from chapter_73 where left_mark <12 and right_mark >13;
select count(id)-1 as depth from chapter_73 where 12 between left_mark and right_mark;

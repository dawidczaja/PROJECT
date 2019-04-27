select depth, hts_code, title from chapter_73 where lft <12 and rght >13;
#select count(id) as depth from chapter_73 where lft <12 and rght >13;
#select count(id)-1 as depth from chapter_73 where 12 between lft and rght;
#select child.hts_code, count(parent.id)-1 as depth from chapter_73 as child, chapter_73 as parent where child.lft between parent.lft and parent.rght group by child.id order by child.lft;
#select concat(repeat('-', count(parent.id)-1), child.hts_code) as hts_code, child.id from chapter_73 as child, chapter_73 as parent where child.lft between parent.lft and parent.rght group by child.id order by child.lft;
#select concat(repeat ('-', (select count(parent.id)-1 from chapter_73 as parent where node.lft between parent.lft and parent.rght)), node.hts_code) as hts_code, title, depth from chapter_73 as node where node.lft between 3 and 24 order by node.lft;

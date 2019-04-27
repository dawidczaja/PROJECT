select id, concat(repeat ('-', 
(select count(parent.id)-1 from chapter_73 as parent 
where node.lft between parent.lft and parent.rght)
), node.hts_code) as hts_code, title, lft, rght, depth from chapter_73 as node 
where node.lft between 3 and 24
order by node.lft;

select id, concat(repeat ('-', 
(select count(parent.id)-1 from chapter_73 as parent 
where node.lft between parent.lft and parent.rght)
), node.hts_code) as hts_code, title, lft, rght, depth from chapter_73 as node 
where node.lft between 10 and 23
order by node.lft;
# '10' i '23' kolejno left_mark i right_ mark; podajac te liczby wyswietlimy dana czesc gałęzi drzewa jakim jest tabela
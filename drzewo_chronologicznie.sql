select count(parent.id)-1 as depth, child.left_mark, child.right_mark, child.hts_code, child.Title from chapter_73 as child, chapter_73 as parent where child.left_mark between parent.left_mark and parent.right_mark group by child.id order by child.left_mark;
#wyswietlenie drzewa chronologicznie wg hts_code
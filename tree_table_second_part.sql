create table Chapter_74 (
Id int(10) not null auto_increment primary key, 
HTS_code varchar(150) not null default'', 
left_mark int(10) not null, 
right_mark int(10) not null,
Depth int(8) not null, 
Title text 
);
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values (74, 1, 40, 0,'Copper and articles thereof');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7412', 2, 7, 1,'Copper tube or pipe fittings (for example, couplings, elbows, sleeves)');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419', 8, 39, 1,'Other articles of copper');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7412.10.0000', 3, 4, 2,'Of refined copper');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7412.20.0000', 5, 6, 2,'Of copper alloys');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.10', 9, 14, 2,'Chain and parts thereof');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.9', 15, 38, 2,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.10.0010', 10, 11, 3,'Hand-made');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.10.0090', 12, 13, 3,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.91', 16, 21, 3,'Cast, moulded, stamped or forged, but not further worked');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99', 22, 37, 3,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.91.0010', 17, 18, 4,'Hand-made');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.91.0090', 19, 20, 4,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.1000', 23, 24, 4,'Cloth (including endless bands), grill and netting, of wire of which no cross-sectional dimension exceeds 6 mm; expanded metal');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.3000', 25, 26, 4,'Springs');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.90', 27, 36, 4,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.9010', 28, 29, 5,'Hand-made');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.909', 30, 35, 5,'Other');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.9091', 31, 32, 6,'Disc (target) with deposition material, consisting of molybdenum silicide, containing 1mg/kg or less of sodium and mounted on a copper or aluminium support');
insert into chapter_74 (HTS_code, left_mark, right_mark, Depth, Title) values ('7419.99.9099', 33, 34, 6,'Other');
select * from chapter_74;
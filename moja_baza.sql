create table Section_XV (Section varchar(10), Chapter int(150), Heading int(150), 
Subheading varchar(150), CN_code varchar(150), Full_code varchar(150), Title_EN text, Title_PL text);
insert into Section_XV (Section, Title_EN, Title_PL) values ("XV", 'Base metals and articles of base metal', 'Metale nieszlachetne i artykuły z metali nieszlachetnych');
insert into Section_XV (Section, Chapter, Title_EN, Title_PL) values ("XV", '73', 'Articles of iron or steel', 'Artykuły z żeliwa lub stali');
insert into Section_XV (Section, Heading, Title_EN, Title_PL) values ("XV", '7307', 'Tube or pipe fittings (for example, couplings, elbows, sleeves), of iron or steel', 'Łączniki rur lub przewodów rurowych (na przykład złączki nakrętne, kolanka, tuleje), z żeliwa lub stali');
insert into Section_XV (Section, Subheading, Title_EN, Title_PL) values ("XV", '7307.1', 'Cast fittings', 'Łączniki odlewane');
insert into Section_XV (Section, Subheading, Title_EN, Title_PL) values ("XV", '7307.11', 'Of non-malleable cast iron', 'Z żeliwa nieciągliwego');
insert into Section_XV (Section, CN_code, Title_EN, Title_PL) values ("XV", '7307.11.10', 'Of a kind used in pressure systems', 'W rodzaju stosowanych w systemach ciśnieniowych');
insert into Section_XV (Section, CN_code, Title_EN, Title_PL) values ("XV", '7307.11.90', 'Other', 'Pozostałe');
insert into Section_XV (Section, Full_code, Title_EN, Title_PL) values ("XV", '7307.11.1000', 'Of a kind used in pressure systems', 'W rodzaju stosowanych w systemach ciśnieniowych');
insert into Section_XV (Section, Full_code, Title_EN, Title_PL) values ("XV", '7307.11.9000', 'Other', 'Pozostałe');


select * from section_XV;
#insert into pracownicy values (2, "jan", "nowak", 3454653, 1977-01-01); 
UPDATE pracownicy
SET data_ur = "1977-01-01"
where imie = "jan";

select * from pracownicy;

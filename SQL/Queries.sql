-- Integrity Constraints in Menu table
select id, count(id) as count
from menu
group by id
having count(id) > 1;

select id 
from menu 
where id is NULL;

select *
from menu
where page_count = 0;

select * from menu
where
sponsor is NULL or "";


-- Check Integrity Contraints in MenuPage Table
select id, count(id) as count
from menupage
 group by id having count(id) > 1;


select id
from menupage
where id is null

select * from menupage
where page_number = 0;


select *
from menu m, menupage p
where m.id = p.menu_id and
p.page_number > m.page_count;


--  Integrity Contraints in MenuItem Table

select id, count(id) as count
from menuitem group by id having count(id) > 1;


select id from menuitem where id is null

select * from menuitem where dish_id = 0;
select * from menuitem where dish_id not in (select id from dish) ;



-- Check Integrity Contraints in Dish Table
select id, count(id) as count
from dish group by id having count(id) > 1;

select id from dish where id is null

select * from dish where (first_appeared not between 1851 and 2018)

select * from dish where lowest_price > highest_price











 

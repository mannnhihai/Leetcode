# Write your MySQL query statement below
select 
s.name
from SalesPerson s
WHERE s.sales_id NOT IN(
    SELECT o.sales_id
    FROM Orders o
inner join Company c
        on o.com_id = c.com_id
where c.name = 'RED');
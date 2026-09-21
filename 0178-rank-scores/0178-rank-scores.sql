# Write your MySQL query statement below
select 
s.score,
(
    select count(distinct  s2.score)
    from scores s2
    where s2.score > s.score
   
) + 1 as 'rank'
from scores s
order by s.score 
desc
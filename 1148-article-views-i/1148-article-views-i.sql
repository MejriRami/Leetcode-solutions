# Write your MySQL query statement below
# Write your MySQL query statement below
select author_id as id 
from  Views v
where v.author_id=v.viewer_id
group by id 
order by id asc;
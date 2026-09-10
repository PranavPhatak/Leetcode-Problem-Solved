# Write your MySQL query statement below
select class from courses group by class having COUNT(student) >= 5
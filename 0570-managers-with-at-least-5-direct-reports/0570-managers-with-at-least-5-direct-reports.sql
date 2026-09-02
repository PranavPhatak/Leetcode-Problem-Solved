# Write your MySQL query statement below
select e.name from employee e join employee emp on e.id = emp.managerid group by e.id having COUNT(e.id) >= 5
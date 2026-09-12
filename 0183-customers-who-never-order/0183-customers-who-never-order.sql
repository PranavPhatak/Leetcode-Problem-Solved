# Write your MySQL query statement below
select c.name as Customers from Customers as c left join Orders as o on c.id = o.customerid where o.customerid is NULL
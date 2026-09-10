# Write your MySQL query statement below
SELECT e.name, b.bonus FROM Employee AS e LEFT JOIN Bonus as b ON e.empId = b.empId where b.bonus < 1000 or b.bonus is NULL
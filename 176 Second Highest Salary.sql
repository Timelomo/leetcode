# Write your MySQL query statement below
# 直接求出最大薪水并排除第一个最大的薪水 剩余的薪水值中最大的就是第二大的
select max(Salary) as SecondHighestSalary from Employee where Salary < (select max(Salary) from Employee)

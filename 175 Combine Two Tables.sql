# Write your MySQL query statement below
# mysql
select FirstName, LastName,City,State from Person left join Address on Person.PersonId = Address.PersonId

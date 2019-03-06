#self join
SELECT x.Name AS Employee
FROM Employee x JOIN Employee y ON (x.ManagerId = y.Id)
WHERE x.Salary > y.Salary

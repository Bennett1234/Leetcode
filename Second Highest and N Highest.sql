#Second Highest Salary
/* this one can not handle when there is not second highest situation
*/
SELECT Salary AS SecondHighestSalary
FROM Employee x
WHERE 1 = (SELECT COUNT(Salary)
          FROM Employee y
          WHERE y.Salary > x.Salary)
/*this one naturally handle the above situation
*/
SELECT max(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary)
                FROM Employee)

# N Highest Salary
SELECT MAX(Salary) #By using MAX we can deal with null situation.
      FROM Employee x
      WHERE (N-1) = (SELECT COUNT(Salary)
          FROM (SELECT DISTINCT Salary #By using DISTINCT to deal with tie situation
                     FROM Employee) y
          WHERE y.Salary > x.Salary)

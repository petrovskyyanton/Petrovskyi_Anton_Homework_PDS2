USE pds;
SELECT DISTINCT JOB_ID, COUNT(EMPLOYEE_ID) as Employees_with_the_same_job FROM employees GROUP BY JOB_ID;
USE pds;
SELECT COUNT(EMPLOYEE_ID) as Employees_from_department_90, AVG(SALARY) as MID_SALARY FROM employees WHERE DEPARTMENT_ID = '90';
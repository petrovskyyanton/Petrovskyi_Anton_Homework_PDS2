USE pds;
SET @London_Location_ID = (SELECT LOCATION_ID FROM locations WHERE CITY ='London');
SET @Department_from_London_ID = (SELECT DEPARTMENT_ID FROM departments WHERE LOCATION_ID = @London_Location_ID);
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM employees WHERE DEPARTMENT_ID = @Department_from_London_ID
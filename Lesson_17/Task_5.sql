USE pds;
SELECT FIRST_NAME, LAST_NAME, employees.DEPARTMENT_ID FROM locations JOIN departments ON locations.LOCATION_ID = departments.LOCATION_ID JOIN employees ON departments.DEPARTMENT_ID = employees.DEPARTMENT_ID WHERE CITY = 'London';

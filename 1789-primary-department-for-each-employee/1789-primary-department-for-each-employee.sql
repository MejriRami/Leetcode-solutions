SELECT 
    e.employee_id,
    IFNULL(
        MAX(CASE WHEN e.primary_flag = 'Y' THEN e.department_id END),
        MIN(e.department_id)
    ) AS department_id
FROM Employee e
GROUP BY e.employee_id;

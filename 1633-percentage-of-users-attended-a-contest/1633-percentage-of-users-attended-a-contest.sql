SELECT 
    contest_id,
    ROUND(
        (SELECT COUNT(*) FROM Register r WHERE r.contest_id = reg.contest_id) 
        / 
        (SELECT COUNT(*) FROM Users) * 100, 
        2
    ) AS percentage
FROM 
    (SELECT DISTINCT contest_id FROM Register) AS reg
ORDER BY 
    percentage DESC,
    contest_id ASC;

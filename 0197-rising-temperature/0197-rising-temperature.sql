/*select w1.id
from Weather w1
where w1.temperature > (
    select w2.temperature from Weather w2 where w2.recorDate = w1.id - 1
);
*/
SELECT w1.id
FROM Weather w1
WHERE w1.temperature > (
    SELECT w2.temperature 
    FROM Weather w2 
    WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
);

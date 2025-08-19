/*SELECT 
    p.product_id,
    ROUND(
        IFNULL(
            SUM(
                CASE 
                    WHEN d.purchase_date BETWEEN p.start_date AND p.end_date 
                    THEN d.units * p.prices 
                    ELSE 0 
                END
            ) / SUM(d.units), 
            0
        ), 
        2
    ) AS average_price
FROM Prices p
LEFT JOIN UnitSol d
    ON p.product_id = d.product_id
GROUP BY p.product_id;
*/
SELECT 
    p.product_id,
    ROUND(
        IFNULL(
            SUM(
                CASE 
                    WHEN d.purchase_date BETWEEN p.start_date AND p.end_date 
                    THEN d.units * p.price
                    ELSE 0
                END
            ) 
            / 
            SUM(
                CASE 
                    WHEN d.purchase_date BETWEEN p.start_date AND p.end_date 
                    THEN d.units
                    ELSE 0
                END
            ),
            0
        ),
        2
    ) AS average_price
FROM Prices p
LEFT JOIN UnitsSold d
    ON p.product_id = d.product_id
GROUP BY p.product_id;

## 3. The With Clause ##

WITH playlist_info AS (
    SELECT
        p.playlist_id playlist_id,
        p.name playlist_name,
        t.name track_name,
        (t.milliseconds / 1000) length_seconds
    FROM playlist p
    LEFT JOIN playlist_track pt ON pt.playlist_id = p.playlist_id
    LEFT JOIN track t ON t.track_id = pt.track_id
    )

SELECT
    playlist_id,
    playlist_name,
    COUNT(track_name) number_of_tracks,
    SUM(length_seconds) length_seconds
FROM playlist_info
GROUP BY playlist_id, playlist_name
ORDER BY playlist_id

## 4. Creating Views ##

CREATE VIEW chinook.customer_gt_90_dollars AS
    SELECT c.* FROM customer c
    LEFT JOIN invoice i ON i.customer_id = c.customer_id
    GROUP BY c.customer_id
    HAVING SUM(i.total) > 90;

SELECT * FROM chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

SELECT * FROM customer_usa

UNION

SELECT * FROM customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

SELECT
    e.first_name || " " || e.last_name employee_name,
    COUNT(inter.customer_id) customers_usa_gt_90
FROM employee e
LEFT JOIN (
    SELECT * FROM customer_usa
    
    INTERSECT
    
    SELECT * FROM customer_gt_90_dollars
    ) inter
    ON inter.support_rep_id = e.employee_id
WHERE e.title = "Sales Support Agent"
GROUP BY employee_name
ORDER BY employee_name

## 7. Multiple Named Subqueries ##

WITH
    india AS (
        SELECT * FROM customer
        WHERE country = "India"
        ),
    sum_total AS (
        SELECT
            c.customer_id customer_id,
            SUM(i.total) total_purchases
        FROM customer c
        INNER JOIN invoice i ON i.customer_id = c.customer_id
        GROUP BY 1
        )

SELECT
    ci.first_name || " " || ci.last_name customer_name,
    st.total_purchases
FROM india ci
INNER JOIN sum_total st ON st.customer_id = ci.customer_id
ORDER BY customer_name


## 8. Challenge: Each Country's Best Customer ##

WITH
    country_sum_total AS (
        SELECT
            c.first_name || " " || c.last_name customer_name,
            c.country country,
            SUM(i.total) total_purchases
        FROM customer c
        INNER JOIN invoice i ON i.customer_id = c.customer_id
        GROUP BY 1,2
        ),
    country_max_purchase AS (
        SELECT
            cst.country country,
            MAX(cst.total_purchases) total_purchased
        FROM country_sum_total cst
        GROUP BY 1
        ),
    country_best_customer AS (
        SELECT
            cmp.country,
            cst.customer_name,
            cmp.total_purchased
        FROM country_max_purchase cmp
        INNER JOIN country_sum_total cst ON (cmp.country = cst.country AND cmp.total_purchased = cst.total_purchases)
            
        )

SELECT
    country,
    customer_name,
    total_purchased
FROM country_best_customer
ORDER BY 1
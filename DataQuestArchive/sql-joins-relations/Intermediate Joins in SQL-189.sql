## 2. Joining Three Tables ##

SELECT t.track_id track_id,
       t.name track_name,
       m.name track_type,
       il.unit_price unit_price,
       il.quantity quantity
FROM track t
INNER JOIN media_type m ON m.media_type_id = t.media_type_id
INNER JOIN invoice_line il ON il.track_id = t.track_id
WHERE il.invoice_id = 4

## 3. Joining More Than Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    ar.name artist_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist ar ON ar.artist_id = al.artist_id
WHERE il.invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    al.title album,
    ar.name artist,
    SUM(il.quantity) tracks_purchased
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN album al ON al.album_id = t.album_id
INNER JOIN artist ar ON ar.artist_id = al.artist_id
GROUP BY album, artist
ORDER BY tracks_purchased DESC
LIMIT 5

## 5. Recursive Joins ##

SELECT
    e1.first_name || " " || e1.last_name employee_name,
    e1.title employee_title,
    e2.first_name || " " || e2.last_name supervisor_name,
    e2.title supervisor_title
FROM employee e1
LEFT JOIN employee e2 ON e2.employee_id = e1.reports_to
ORDER BY employee_name

## 6. Pattern Matching Using Like ##

SELECT
    c.first_name first_name,
    c.last_name last_name,
    c.phone phone
FROM customer c
WHERE c.first_name LIKE "%belle%"


## 7. Generating Columns With The Case Statement ##

SELECT
    c.first_name || " " || c.last_name customer_name,
    COUNT(i.invoice_id) number_of_purchases,
    SUM(i.total) total_spent,
    CASE
        WHEN SUM(i.total) < 40 THEN "small spender"
        WHEN SUM(i.total) > 100 THEN "big spender"
        ELSE "regular"
        END
        AS customer_category
FROM customer c
INNER JOIN invoice i ON i.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY customer_name
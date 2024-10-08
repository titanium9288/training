-- 코드를 입력하세요
SELECT
    CAST(DATE_FORMAT(DATETIME, "%k") AS SIGNED) AS HOUR,
    COUNT(*)
FROM 
    ANIMAL_OUTS
GROUP BY
    HOUR
HAVING 
    HOUR BETWEEN 9 AND 19
ORDER BY
    HOUR ASC
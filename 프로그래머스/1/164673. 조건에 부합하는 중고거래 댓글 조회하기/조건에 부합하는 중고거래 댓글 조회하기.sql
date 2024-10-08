-- 코드를 입력하세요
SELECT 
    TITLE, 
    r.BOARD_ID, 
    REPLY_ID, 
    WRITER_ID, 
    CONTENTS, 
    DATE_FORMAT(r.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM 
    USED_GOODS_REPLY r
JOIN (
    SELECT 
        TITLE, 
        BOARD_ID,
        CREATED_DATE AS BOARD_DATE
    FROM USED_GOODS_BOARD
    ) b ON r.BOARD_ID = b.BOARD_ID
WHERE 
    DATE_FORMAT(b.BOARD_DATE, "%Y-%m") = "2022-10"
ORDER BY 
    r.CREATED_DATE ASC,
    b.TITLE ASC
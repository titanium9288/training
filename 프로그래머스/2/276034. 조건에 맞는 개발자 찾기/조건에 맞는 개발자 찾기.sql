SELECT 
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM 
    DEVELOPERS
WHERE
    SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = "Python") != 0
OR  SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = "C#") != 0
ORDER BY
    ID ASC

# 아래는 위에 걸 풀고 찾은 참고용 코드.
# JOIN에 조건을 달 수 있는지 몰랐다

# SELECT 
#     *
# FROM 
#     DEVELOPERS d
# JOIN 
#     SKILLCODES s ON (d.SKILL_CODE & s.CODE) = s.CODE
# WHERE 
#     s.NAME IN ('Python', 'C#')
# ORDER BY 
#     d.ID ASC;
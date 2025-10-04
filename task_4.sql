-- FILE: task_4.sql
-- STEP: Print full description of the books table (case-insensitive)

SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
AND LOWER(TABLE_NAME) = 'books';


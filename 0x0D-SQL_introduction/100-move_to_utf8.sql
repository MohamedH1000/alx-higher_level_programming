-- a hbtn_0c_0 database to UTF8 to be converted (utf8mb4, collate utf8mb4_unicode_ci) 
-- a hbtn_0c_0 database to UTF8 to be converted
USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

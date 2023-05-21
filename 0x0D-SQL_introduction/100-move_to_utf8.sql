-- Convert hbtn_0c_0 DB to UTF8 encoding.
-- SPECS:
--	a. The hbtn_0c_0 DB must be converted.
--	b. The first_table table must be converted.
--	c. The name field in first_table must be converted.

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

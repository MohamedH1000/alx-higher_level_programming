-- the data base and the user to be created
-- the database and the user to be created
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- lets see
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
-- lets see
FLUSH PRIVILEGES;

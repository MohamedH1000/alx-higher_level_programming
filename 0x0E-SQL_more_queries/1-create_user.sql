-- the my sql server first user to be created
-- the my sql erver seconed user to be created
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;
FLUSH PRIVILEGES;

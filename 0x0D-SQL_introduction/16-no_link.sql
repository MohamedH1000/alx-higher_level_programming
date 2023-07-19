-- all the record of the table second table to be listed
-- a row without a name value not to be listed
SELECT score, name 
FROM second_table
WHERE name <> ''
ORDER by 1 DESC;

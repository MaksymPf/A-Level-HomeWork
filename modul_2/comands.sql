https://github.com/Bandydan/Postgres/blob/master/psql4.md

№ 2

modul=# SELECT 'This is ' || name || ', ' || CASE WHEN gender ='m' THEN 'he' ELSE 'she' END|| ' has email ' || email AS info FROM people;

                     info
-----------------------------------------------
 This is Vasya, he has email mmm@mmail.com
 This is Alex, he has email mmm@gmail.com
 This is Alexey, he has email alexey@gmail.com
 This is Helen, she has email hell@gmail.com
 This is Jenny, she has email eachup@gmail.com
 This is Lora, she has email tpicks@gmail.com
(6 rows)

№ 3

modul=# SELECT 'We have ' || gender || ' ' || CASE WHEN gender ='m' THEN 'boys' ELSE 'girls' END || '!' AS gender_info FROM people;

SELECT gender, COUNT(*) FROM people GROUP BY gender;
SELECT COUNT(*), gender FROM people GROUP BY gender;
SELECT COUNT(gender) FROM people GROUP BY gender;

modul=# SELECT 'We have ' || COUNT(gender) || ' ' || CASE WHEN gender ='m' THEN 'boys' ELSE 'girls' END || '!' AS gender_info FROM people GROUP BY gender;

   gender_info
------------------
 We have 3 boys!
 We have 3 girls!
(2 rows)

№ 4

modul=# SELECT name, vocabulary_id FROM vocabulary LEFT JOIN word ON (vocabulary.id = word.vocabulary_id);

^заджоинит таблицу и вернет 50 строк

modul=# SELECT name, COUNT(vocabulary_id) FROM vocabulary LEFT JOIN word ON (vocabulary.id = word.vocabulary_id) GROUP BY name;

modul=# SELECT name, COUNT(vocabulary_id) AS words FROM vocabulary LEFT JOIN word ON (vocabulary.id = word.vocabulary_id) GROUP BY name;
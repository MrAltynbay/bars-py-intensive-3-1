MVCC.
1) Что произойдет со строками, если выполняется ROLLBACK транзакции?
Отмена изменений работает аналогично фиксации, только в XACT(это файлы в каталоге PGDATA/pg_xact.
В них для каждой транзакции отведено два бита: committed и aborted )
для транзакции выставляется бит aborted. Отмена выполняется так же быстро, как и фиксация. Хоть команда и называется ROLLBACK, отката изменений не происходит: все, что транзакция успела изменить в страницах данных, остается без изменений.
2) Выполнить sql запросы в двух процессах для таблицы workers:
			Процесс 1								Процесс 2
BEGIN;									|
------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO category(id, name) VALUES (1,'Мучное');			|
INSERT INTO category(id, name) VALUES (3,'Игрушки');			|
------------------------------------------------------------------------------------------------------------------------------------
UPDATE category SET name = name || id;					|
------------------------------------------------------------------------------------------------------------------------------------
SELECT * FROM heap_page('category',0);					|SELECT *, xmin, xmax from category;
									|
									|
									|Изменений в таблице нет, потому что не было COMMIT; у 1 
									|транзакции
									|
									|
									|
ctid     state  xmin    xmax t_ctid					|
"(0,11)",normal,690,690,"(0,14)"					|
"(0,12)",normal,690,690,"(0,15)"					|
									|
Эти 2 строки сверху это добавление в таблицу с INSERT			|
									|
"(0,13)",normal,690,0 (a),"(0,13)"					|
"(0,14)",normal,690,0 (a),"(0,14)"					|
"(0,15)",normal,690,0 (a),"(0,15)"					|
									|
Апдейтнулись 3 строки, у них (a) еще не закомичены			|
------------------------------------------------------------------------------------------------------------------------------------
COMMIT;									|Все изменения появились
------------------------------------------------------------------------------------------------------------------------------------
BEGIN;									|BEGIN;	
------------------------------------------------------------------------------------------------------------------------------------
UPDATE category SET name = '''' || name || '''';			|UPDATE category SET name = '''' || name || '''';
									|
3 rows affected in 2 ms							|Тут бесконечная прогрузка, которая не завершается
									|Как только закоммитился 1ая транзакция эта команда сразу выполнилась

------------------------------------------------------------------------------------------------------------------------------------
COMMIT;									|COMMIT;	
									|
Обернулось все в 1 кавычку						|Обернулось уже в 2 кавычки

Блокировки
1) В двух транзакциях добиться блокировки строки при попытке обновления одной и той же записи.
И с помощью представления pg_lock получить информацию о получившейся блокировке.
Скрин отдельно пришлю результата

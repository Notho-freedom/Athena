from PySide6.QtSql import *

def createConnection():
	def check(func, *args):
		if not func(*args):
			raise ValueError(func.__self__.lastError())

	db = QSqlDatabase.addDatabase("QSQLITE")
	db.setDatabaseName(":memory:")
	check(db.open)
	query = QSqlQuery(db)
	query.exec("create table employee(id int primary key, name varchar(20), city int, country int)")
	query.exec("insert into employee values(1, 'Espen', 5000, 47)")
	query.exec("insert into employee values(2, 'Harald', 80000, 49)")
	query.exec("insert into employee values(3, 'Sam', 100, 1)")
	query.exec("create table city(id int, name varchar(20))")
	query.exec("insert into city values(100, 'San Jose')")
	query.exec("insert into city values(5000, 'Oslo')")
	query.exec("insert into city values(80000, 'Munich')")
	query.exec("create table country(id int, name varchar(20))")
	query.exec("insert into country values(1, 'USA')")
	query.exec("insert into country values(47, 'Norway')")
	query.exec("insert into country values(49, 'Germany')")
	model = QSqlRelationalTableModel()
	model.setTable("employee")
	print(model.select())
createConnection()
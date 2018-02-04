----------A note for myself-----------
How to run the mysql and the py script on my own mac
1. Install mysql client: 
	install homebrew first via terminal:
	/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	then install mysql via brew:
	brew install mysql
2. Install python MySQLdb module via terminal:
	pip install mysql-python
	if permission denind, try this:
	pip install mysql-python
3. Ensure run the python script in 2.7 version. Python 3.6 doesn't support MySQLdb module.

Here is the cheatsheet to mysql 
connect：mysql -u seniordesign -p -h den1.mysql5.gear.host
password：00000！
show databases;
use seniordesign;
show tables;
select * from emr；
Don't forget to type ; before return.
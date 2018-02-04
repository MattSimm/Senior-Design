# A note for myself

## How to run the mysql and the py script on my own mac.

### 1. Install mysql client: 

First install homebrew:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then install mysql:

```
brew install mysql
```

### 2. Install python MySQLdb module:

```
pip install mysql-python
```

if permission denind, try this:

```
endo pip install mysql-python
```

### 3. This is for python 2.7 version, run it through mac defautly.

## Here is the cheatsheet to mysql 
```
connect：mysql -u seniordesign -p -h den1.mysql5.gear.host
password：00000！
show databases;
use seniordesign;
show tables;
select * from emr；
```
**Don't forget to type ';' before return.**

Or see more on:
* [W3Schools](https://www.w3schools.com/sql/default.asp)
* [My simply MySQL Command Line Cheatsheet](https://gist.github.com/hofmannsven/9164408)

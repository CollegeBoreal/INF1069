# INF1069

### SGBD:

. lancer le CLI (Command Level Interface) de MySQL

```
mysql> CREATE DATABASE etudiants;
mysql> CREATE USER 'etudiants'@'localhost' IDENTIFIED BY 'etudiants_1';
mysql> GRANT ALL ON etudiants.* TO 'etudiants'@'localhost';
```

Dump

```
mysqldump --skip-lock-tables -u etudiants -p etudiants > etudiants.sql
Test

```

###

```
mysql> select * from rental where rental_date between '2005-08-23 01:00:00' and '2005-08-23 02:00:00' and return_date between '2005-08-23 23:00:00' and '2005-08-23 23:59:00';
```

```
select * from rental where rental_date >= '2005-08-23 01:00:00' and rental_date <= '2005-08-23 02:00:00' and return_date >= '2005-08-23 23:00:00' and return_date <= '2005-08-23 23:59:00'; 
```

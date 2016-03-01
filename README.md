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

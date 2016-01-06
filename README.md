Brice# INF1069

### SGBD:

. installer and démarrer MySQL (mysql.server start)
```
$ create database etudiants;
$ create user 'etudiants'@'localhost' identified by 'etudiants_1';
$ grant all on etudiants.* to 'etudiants'@'localhost';
```

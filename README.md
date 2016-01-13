jour
# INF1069

### SGBD:

. installer and démarrer MySQL (mysql.server start)
Initialiser le mot de passe de l'utilisateur root a "password"

. lancer la commande ci-dessous dans le terminal

```
$ mysql -u root -ppassword
```

. lancer le CLI (Command Level Interface) de MySQL

```
mysql> create database etudiants;
mysql> create user 'etudiants'@'localhost' identified by 'etudiants_1';
mysql> grant all on etudiants.* to 'etudiants'@'localhost';
```

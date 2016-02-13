
### Installation Manuelle:

. Aller sur le site de My communaute MySQL 

http://dev.mysql.com/downloads/mysql/

Telecharger la version de votre plateforme (i.e. Mac OSX)

. installer and démarrer MySQL (mysql.server start)

. Initialiser le mot de passe de l'utilisateur root a "password"

Sauver le mot passe donné par MySQL Installation

. Initialiser les commandes MySQL sur le "path"

```
vi ~/.bash_profile
```

Ajouter 

```
export PATH=/usr/local/mysql/bin:$PATH
```

. lancer la commande ci-dessous dans le terminal

```
$ mysql -u root -p<le mot de passe apres l'installation>
```

. lancer le CLI (Command Level Interface) de MySQL et changer le mot de passe de root

````
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```


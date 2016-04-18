# Pratique de manipulation de données

### Example de bases de données
http://dev.mysql.com/doc/index-other.html

### Fichier sakila-db
. Télécharger le fichier world.sql dans le répertoire racine du projet.

http://downloads.mysql.com/docs/sakila-db.zip

. Décompresser le fichier

### Charger les données dans Docker 

- remplacer le <PWD>

- Créer la base de données sakila

```
$ docker exec -it INF1069-mysql mysql -u root -p -e "create database sakila;"
```

- Créer l'utilisateur etudiants

```
$ docker exec -it INF1069-mysql \
 mysql -u root -p -e "GRANT ALL PRIVILEGES on sakila.* TO 'etudiants'@'localhost' IDENTIFIED BY 'etudiants_1' WITH GRANT OPTION;"
```

- Charger la base

```
$ docker exec  -i INF1069-mysql  mysql -u etudiants -p<MDP> sakila < ~/sakila-db/sakila-schema.sql
```

- Charger les données

```
$ docker exec  -i INF1069-mysql  mysql -u etudiants -p<MDP> sakila < ~/sakila-db/sakila-data.sql
```

### Éxécuter les commandes SQL de BlackBoard

![alt tag](https://github.com/CollegeBoreal/INF1069-16H/blob/master/7.DML_AVANCE/sakila.png)

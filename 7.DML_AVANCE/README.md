# Pratique de manipulation de données

### Example de bases de données
http://dev.mysql.com/doc/index-other.html

### Fichier sakila-db
. Télécharger le fichier world.sql dans le répertoire racine du projet.

http://downloads.mysql.com/docs/sakila-db.zip

. Décompresser le fichier

### Charger les données dans Docker 

- remplacer le <PWD>

- Charger la base

```
$ docker exec  -i INF1069-mysql  mysql -u etudiants -p<MDP> world < ~/sakila-db/sakila-schema.sql
```

- Charger les données

```
$ docker exec  -i INF1069-mysql  mysql -u etudiants -p<MDP> world < ~/sakila-db/sakila-data.sql
```

### Éxécuter les commandes SQL de BlackBoard

![alt tag](https://github.com/CollegeBoreal/INF1069-16H/blob/master/7.DML_AVANCE/sakila.png)

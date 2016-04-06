# Performance

# Index

# Plan d'execution


# Pratique de manipulation de données

### Example de bases de données
http://dev.mysql.com/doc/index-other.html

### Fichier employees-db
. Télécharger le fichier employees.sql dans le répertoire racine du projet.

. Décompresser le fichier

### Charger les données dans Docker 

- remplacer le <PWD>

- Créer la base de données employees

- Charger la base

```
$ docker exec  -i INF1069-mysql  mysql -u etudiants -p<MDP> employees < ~/employees_db/employees.sql
```


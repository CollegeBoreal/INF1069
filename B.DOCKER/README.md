# Docker

# Installation

. Installer Docker Toolbox

https://www.docker.com/products/docker-toolbox

. Installer INF1069 dans le dossier ~/Developer

```
$ git clone git@github.com:CollegeBoreal/INF1069-16H.git
```

. changer de repertoire

```
$ cd INF1069-16H
```

. Installer MySQL

```
$ docker run --name INF1069-mysql -e MYSQL_ROOT_PASSWORD=password -v ~/Developer/INF1069-16H:/Developer/INF1069-16H -d mysql:latest 
```

. Executer la commande d'accer a MySQL

```
$ docker exec -it INF1069-mysql bash
```

## Commandes utiles

```
$ docker search ubuntu // Chercher une image
$ docker pull ubuntu // telecharger image
$ docker images // Liste de toutes les images
$ docker ps // Liste de tous les containers
$ docker ps -a // Liste de tous les containers incluant les containers arretes
$ docker rm // Enleve un container
$ docker rmi // Enleve une image
$ docker rm `docker ps -a -q` // Enleve tous les containers
$ docker history nom_image // list l'histoire d'une image
$ docker info // Recupere docker info
```

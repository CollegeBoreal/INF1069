# Docker

# Installation

. Installer Docker Toolbox

https://www.docker.com/products/docker-toolbox

. Installer INF1069 dans le dossier ~/Developer

```
$ git clone git@github.com:setrar/INF1069.git
```

. changer de repertoire

```
$ cd INF1069
```

. Installer MySQL

```
$ docker run --name INF1069-mysql -e MYSQL_ROOT_PASSWORD=password -v ~/Developer/INF1069:/Developer/INF1069 -d mysql:latest 
```

. Executer la commande d'accer a MySQL

```
$ docker exec -it INF1069-mysql bash
```

## Commandes utiles

```
$ docker search centos // It will help you to search one image
$ docker pull centos // It will help you to download one image
$ docker images // it will list all images which you have
$ docker ps // it will show all running containers
$ docker ps -a // it will show all containers
$ docker rm // it will remove container
$ docker rmi // it will remove image
$ docker rm `docker ps -a -q` // it will remove all containers
$ docker history image_name // list image's history
$ docker info // get docker info
```

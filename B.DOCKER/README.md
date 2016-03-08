# Docker

## Installation Machine Hôte (Windows, Mac OS X)

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

## Installation Nuage [ATIR - Ubuntu Trusty 14.04 (LTS)]

https://docs.docker.com/engine/installation/linux/ubuntulinux/

### Update your apt sources
```
 $ apt-get update
 $ apt-get install apt-transport-https ca-certificates
```
### Add the new GPG key.

```
$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```

### Add an entry for your Ubuntu operating system.

- On Ubuntu Trusty 14.04 (LTS)

```
echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > sudo /etc/apt/sources.list.d/docker.list
```

- Ubuntu Wily 15.10

```
echo "deb https://apt.dockerproject.org/repo ubuntu-wily main" > sudo /etc/apt/sources.list.d/docker.list
```

### Update the APT package index.

```
$ apt-get update
```

### Purge the old repo if it exists.
```
$ apt-get purge lxc-docker
```

### Verify that APT is pulling from the right repository.
```
$ apt-cache policy docker-engine
```

### AUFS Storage Driver for Wily and Trusty
```
$ sudo apt-get install linux-image-extra-$(uname -r)
```

### AppArmor for Trusty
```
$ sudo apt-get install apparm
```

## Installer le moteur Docker
```
$ sudo apt-get install docker-engine
$ sudo service docker start
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


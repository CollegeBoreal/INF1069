# Docker

# Installation

. Installer Docker Toolbox

https://www.docker.com/products/docker-toolbox

. Installer INF1069 dans le dossier ~/Developer

```
$ git clone 
```

. changer de repertoire

```
$ cd INF1069
```

. Installer MySQL

```
$ docker run --name INF1069-mysql -e MYSQL_ROOT_PASSWORD=password -v ~/Developer/INF1069:/Developer/INF1069 -d mysql:latest 
```

. 

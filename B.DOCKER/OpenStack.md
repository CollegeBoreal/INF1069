# OpenStack


## On Mac

```
$ sudo easy_install pip
$ sudo -H pip install python-openstackclient --upgrade --ignore-installed six
```

### [ImportError: No module named xmlrpc_client] issue

```
$ sudo -H pip uninstall python-novaclient
$ sudo easy_install python-novaclient
```

### Testing Nova Commands

```
$ nova --version
$ nova floating-ip-pool-list
$ nova image-list
$ nova flavor-list
```
## Set your environment Variables

```
$ source ~/Developer/canarie.ca/collège-boréal-openrc-quebec.sh
```

http://docs.openstack.org/user-guide/common/cli_set_environment_variables_using_openstack_rc.html

## Create the Docker Machine on OpenStack

```
$ docker-machine --debug \
  create --driver openstack \
         --openstack-flavor-name m1.tiny \
         --openstack-image-name "Ubuntu 14.04" \
         --openstack-ssh-user ubuntu \
         --openstack-sec-groups default \
    INF1069
```



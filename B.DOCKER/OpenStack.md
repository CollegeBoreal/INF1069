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
$ nova --version
```

http://docs.openstack.org/user-guide/common/cli_set_environment_variables_using_openstack_rc.html

```
$ docker-machine --debug create \ 
    --driver openstack \
    --openstack-flavor-name m1.tiny \
    --openstack-image-name "Ubuntu 14.04" \
    --openstack-ssh-user ubuntu \
    --openstack-endpoint-type publicURL \
    --openstack-sec-groups default 
    INF1069
```

### Nova Commands

```
$ nova floating-ip-pool-list
$ nova image-list
$ nova flavor-list
```

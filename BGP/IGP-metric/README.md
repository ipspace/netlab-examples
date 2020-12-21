# Interaction between IBGP and IGP metrics

This directory contains topology files, Vagrantfile, Ansible inventory, and router configurations for a simple network illustrating the interaction between IBGP and multiple IGPs.

![Network diagram](https://blog.ipspace.net/2021/01/BGP-IGP-metric.png)

You could use router configurations from the `config` directory (EIGRP + OSPF combo) or follow this recipe that works out-of-the box with *vagrant-libvirt* (some assembly required for other environments):

* Add **[netsim-tools](https://github.com/ipspace/netsim-tools)** to your path
* Create Ansible and Vagrant configuration files with **create-topology -t _filename_ -g -c -i**
* Create virtual lab with **vagrant up**
* Deploy initial IP addressing with **initial-config.ansible**
* Deploy BGP with **config.ansible -e config=igp**
* Deploy BGP with **config.ansible -e config=bgp**

Sample topology files:

*topology-ospf.yml*
: OSPF-only topology

*topology-2igp.yml*
: Network-wide OSPF + EIGRP between PE1 and E1

*topology-isis.yml*
: Network-wide IS-IS + OSPF between PE1 and E1. The IGP configuration templates can be used with Cisco IOS, Arista vEOS, or Cisco Nexus OS -- just change the device type of PE1 in the topology file.

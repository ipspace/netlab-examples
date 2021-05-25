# Interaction between IBGP and IGP metrics

This directory contains topology files, Vagrantfile, Ansible inventory, and router configurations for a simple network illustrating the interaction between IBGP and multiple IGPs.

![Network diagram](https://blog.ipspace.net/2021/01/BGP-IGP-metric.png)

You could use router configurations from the `config` directory (EIGRP + OSPF combo) or follow this recipe that works out-of-the box with *vagrant-libvirt* (some assembly required for other environments):

* [Install *netsim-tools*](https://netsim-tools.readthedocs.io/en/latest/install.html) and add the top directory to your path.
* Create Ansible and Vagrant configuration files with **create-topology -t _filename_ -g -c -i**
* Create virtual lab with **vagrant up**
* Deploy device configurations with **initial-config.ansible**

**Notes:**

* EIGRP is supported in *netsim-tools* in release 0.7. You might have to switch to *dev_0.7* branch until the release is published.
* To run your tests with a different virtualization provider, add **provider: virtualbox** or **provider: clab** to the topology file(s).

Sample topology files:

*topology-ospf.yml*
: OSPF-only topology

*topology-2igp.yml*
: Network-wide OSPF + EIGRP between PE1 and E1

*topology-isis.yml*
: Network-wide IS-IS + OSPF between PE1 and E1. To check the behavior of various network operating systems, replace **device: csr** with the [network device of your choice](https://netsim-tools.readthedocs.io/en/latest/platforms.html).
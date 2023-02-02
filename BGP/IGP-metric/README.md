# Interaction between IBGP and IGP metrics

This directory contains topology files, Vagrantfile, Ansible inventory, and router configurations for a simple network illustrating the interaction between IBGP and multiple IGPs.

![Network diagram](https://blog.ipspace.net/2021/01/BGP-IGP-metric.png)

You could use router configurations from the `config` directory (EIGRP + OSPF combo) or follow this recipe that works out-of-the box with *vagrant-libvirt* (some assembly required for other environments):

* [Install *netlab*](https://netsim-tools.readthedocs.io/en/latest/install.html).
* Start the lab with **netlab up _topology-file_**

Sample topology files:

* *topology-ospf.yml*: OSPF-only topology on Cisco IOSv
* *topology-2igp.yml*: Network-wide OSPF + EIGRP between PE1 and E1 on Cisco IOSv
* *topology-isis.yml*: Network-wide IS-IS + OSPF between PE1 and E1 on Arista vEOS. 

**Notes:**

* To run your tests with a different virtualization provider, execute **netlab up** with **-p _provider_** argument.
* To check the behavior of various network operating systems, execute **netlab up** with **-d _device_** argument using any [network device of your choice](https://netsim-tools.readthedocs.io/en/latest/platforms.html).

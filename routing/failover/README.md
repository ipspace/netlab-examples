# Link Failure Failover Testing

The following network topology was built with vagrant-libvirt provider on a Ubuntu machine using P2P UDP tunnels emulating Ethernet links:

![](igp-failover-topology.png)

Challenge: what exactly happens when one of the primary links fails?

## Try it out

* Clone the repository.
* [Install *netsim-tools*](https://netsim-tools.readthedocs.io/en/latest/contribute.html)
* Get Cisco IOS boxes for your Vagrant environment. For more extensive modifications [read this first](https://netsim-tools.readthedocs.io/en/latest/).
* It should be trivial to replace IOS devices with other network devices -- *netsim-tools* supports OSPF on all supported platforms.
* Execute **netlab create** to create Vagrantfile, Ansible inventory, and Ansible configuration file.
* Start the topology with **vagrant up**
* Deploy initial IP configuration with **netlab initial**
* Deploy OSPF configuration with **netlab config routing-ospf**
* Enjoy!
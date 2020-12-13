# Link Failure Failover Testing

The following network topology was built with vagrant-libvirt provider on a Ubuntu machine using P2P UDP tunnels emulating Ethernet links:

![](igp-failover-topology.png)

Challenge: what exactly happens when one of the primary links fails?

## Try it out

* Clone the repository. Include the **tools** submodule.
* Get Cisco IOS boxes for your Vagrant environment. For more extensive modifications [read this first](https://netsim-tools.readthedocs.io/en/latest/), in particular the description of the **create-topology** tool. It should be trivial to replace IOS devices with Nexus-OS devices as I already created the OSPF routing configuration template.
* Adjust `Vagrantfile` if needed. You will have to rewrite it completely for non-libvirt environments (feel free to submit pull requests once you get it done).
* Start the topology with **vagrant up**
* Deploy initial IP configuration with **initial-config.ansible** (hint: add **tools** directory to PATH)
* Deploy OSPF configuration with **config.ansible -e config=routing-ospf**
* Enjoy!
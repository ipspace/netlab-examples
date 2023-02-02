# Anycast Lab: OSPF+MPLS

This lab was used to [debunk the _anycast doesn't work with MPLS/LDP_ claim](https://blog.ipspace.net/2021/11/anycast-mpls.html).

![Lab topology](MPLS-anycast-ospf-topo.png)

To start the lab:

* [Install the prerequisite software](https://netsim-tools.readthedocs.io/en/latest/install/ubuntu.html) (netlab, Ansible, libvirt+KVM) on a Ubuntu server.
* Create [Arista vEOS Vagrant box](https://netsim-tools.readthedocs.io/en/latest/labs/eos.html)
* Execute **netlab up**

Alternatively, you can take the [configuration tarball](anycast-mpls-ospf.tar.gz), extract it into an empty directory, and start  the lab with *containerlab* (but then you won't have a [working MPLS data plane](https://blog.ipspace.net/2022/03/dataplane-quirks-virtual-devices.html)).

# Anycast Lab: BGP AddPath

This lab was used to [describe how you can implement BGP-based anycast with BGP Additional Paths functionality](https://blog.ipspace.net/2021/12/bgp-anycast-lab.html).

![Lab topology](graph.bgp.png)

**Note**: The BGP topology does not show the IBGP sessions between the anycast nodes that are not established anyway.

To start the lab:

* [Install the prerequisite software](https://netsim-tools.readthedocs.io/en/latest/install.html#creating-the-lab-environment).
* Build [Cisco IOSv](https://netsim-tools.readthedocs.io/en/latest/labs/iosv.html) or [Cisco CSR](https://netsim-tools.readthedocs.io/en/latest/labs/csr.html) Vagrant box.
* Execute **netlab up**

If you want to rebuild the lab on another platform, you might find the final router configurations useful: 

* [IBGP AddPath with next-hop-self on AS edge routers](ios-config-addpath.tgz)
* [IBGP AddPath with external BGP next hops](ios-config-addpath-external-next-hop.tgz)

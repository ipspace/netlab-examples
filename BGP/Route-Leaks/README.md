# Exercise: Fix BGP Route Leaks

This directory contains the [*netlab* topology file](topology.yml) that you can use to practice BGP security tools. For more details, see blog.ipspace.net.

![Lab topology](leak-practice-lab.png)

The directory contains two other topology files you can use to explore how netlab-generated graphs work:

* [nice-graph.yml](nice-graph.yml) changes the order of node-to-link attachments to ensure the nodes higher up in the AS hierarchy are always listed first, resulting in a graph that better reflects the roles of autonomous systems
* [graph-rank.yml](graph-rank.yml) uses new **graph.rank** node attribute (available in _netlab_ release 25.10 and later) to generate an almost-perfect graph (the above diagram).

## Changing Device Types

The lab topology is using FRR containers, and the custom configuration templates that set BGP local preference is available for FRR, Cumulus Linux and Arista EOS.

You can use the lab with any other supported device, but unless you'll create a custom configuration template for your device you'll experience failures in the final step of the device configuration. Ignore them ;)

Use `-p` **netlab up** parameter to change the virtualization provider and `-d` parameter to change the device type. For example, use the following command to start the lab with Cisco IOSv as the customer router:

```
netlab up -p libvirt -d iosv
```

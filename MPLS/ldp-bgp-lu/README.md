# MPLS LDP + BGP-LU Lab

This lab combines LDP within AS 65000 with BGP LU across three autonomous systems (AS 65000, AS 65101 and AS 65102):

![BGP sessions](topology.bgp.png)

The central autonomous system has a route reflector and a P-router that is not running BGP:

![Physical lab topology](topology.link.png)

The lab topology uses a mix of Cisco IOSv and Arista vEOS devices with *libvirt* provider.

To test MPLS configuration module with other devices without changing the lab topology file, change the PE1 device type with `-s` argument of **netlab up** command:

```
netlab up -s nodes.pe1.device=<type>
```

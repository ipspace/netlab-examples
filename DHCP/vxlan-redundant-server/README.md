# VXLAN DHCP relaying with redundant DHCP servers

This directory contains *netlab* topology file used to test DHCP relaying from an VXLAN segment
a set of redundant DHCP servers in the network core.

![DHCP relaying topology](vxlan-redundant-dhcp-server.png)

After starting the lab, the clients (*cl_a* and *cl_b*) should get DHCP-assigned IP address on their lab-facing interfaces.

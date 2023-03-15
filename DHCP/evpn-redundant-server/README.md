# Inter-VRF DHCP relaying with redundant DHCP servers

This directory contains *netlab* topology file used to test DHCP relaying from an EVPN VRF toward
a set of redundant DHCP servers in the network core.

![DHCP relaying topology](evpn-dhcp-redundant-server.png)

After starting the lab, the clients (*cl_a* and *cl_b*) should get DHCP-assigned IP address on their lab-facing interfaces.

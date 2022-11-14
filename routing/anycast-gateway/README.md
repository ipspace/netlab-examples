# IRB with Anycast Gateways

This directory contains *netlab* topology file for a simple VLAN trunking scenario with two VLANs stretched across two switches. Both switches are running IRB on both VLANs, and use static anycast gateway to give the VLAN hosts consistent first-hop gateway.

![Anycast gateway topology](anycast-gateway.png)

After starting the lab, all hosts should be able to ping each other.

## Changing Device Types

This topology can be used with all network devices supporting VLANs and anycast gateways:

* To change the switch device type, use `-s groups.switches.device=xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

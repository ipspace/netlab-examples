# VXLAN bridging

This directory contains *netlab* topology file for a simple VXLAN bridging scenario -- two VLANs bridged across an IP underlay network.

![VXLAN bridging topology](vxlan-bridging.png)

After starting the lab, h1 should be able to ping h2, and h3 should be able to ping h4, but there should be no traffic routed between the VLANs. Also, the VLAN hosts should not be able to access the switches.

## Changing Device Types

This topology can be used with all network devices supporting VLAN, VXLAN, and OSPF configuration modules, and all virtualization providers supported by *netlab*:

* To change the switch device type, use `-s groups.switches.device=xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

For example, to start the lab with Arista EOS devices running in _containerlab_, use:

```
netlab up -p clab -s groups.switches.device=eos
```

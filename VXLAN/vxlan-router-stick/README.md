# VXLAN Router-on-a-Stick

This directory contains *netlab* topology file for a VXLAN router-on-a-stick scenario doing VXLAN-to-VXLAN routing between a set of VXLAN-enabled VLAN interfaces.

![VXLAN router-on-a-stick topology](netlab-vxlan-router-stick.png)

After starting the lab, *h1* should be able to ping *h2*.

## Changing Device Types

This topology can be used with all network devices supporting VLAN, VXLAN, and VRF configuration modules, and all virtualization providers supported by *netlab*:

* To change all devices in the topology (apart from Linux hosts), use the `-d xxx` CLI argument
* To change the switch device type, use `-s groups.switches.device=xxx` CLI argument
* To change the router device type, use `-s groups.routers.device=xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

For example, to start the lab with Cumulus VX devices, use:

```
netlab up -d cumulus
```

# Using BGP Pipe

This directory contains the *netlab* topology file for a lab with a BGP router and a Linux host running BGP Pipe. It also contains a Dockerfile to build a container with BGP Pipe.

You'll find more details in [this blog post](https://blog.ipspace.net/2024/08/netlab-bgpipe/).

## Changing Device Types

The lab topology uses FRRouting running as a container. It can be used with any device supported by the netlab BGP configuration module and *libvirt* or *clab* virtualization provider:

* To change device type, use the `-d xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

For example, to start the lab with a Nexus OS virtual machine, use:

```
netlab up -d nxos -p libvirt
```

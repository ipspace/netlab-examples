# VRF Lite with Hosts Test Cases

This directory contains *netsim-tools* topology files describing several simple VRF Lite test cases containing a set of hosts attached to a single router.

The test cases can be used with all network devices supporting VRF configuration module and all virtualization providers supported by *netsim-tools*:

* To change the router device type, use `-s nodes.rtr.device=xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

To start the lab with Cisco IOSv router, use:

```
netlab up -s nodes.rtr.device=iosv <topo-name>
```

To start the lab with Cisco IOS XE router, use:

```
netlab up -s nodes.rtr.device=csr <topo-name>
```

To start the lab with Arista cEOS (using *containerlab*) use:

```
netlab up -s nodes.rtr.device=eos -p clab <topo-name>
```

## Isolated VRFs

The `multi-vrf.yml` topology contains two isolated VRFs:

* VRF *red* containing Linux hosts h1 and h2
* VRF *blue* containing Linux hosts h3 and h4

After starting the lab, h1 should be able to ping h2 but not h3 or h4, and h3 should be able to ping h4 but not h1 or h2.

## Inter-VRF Route Leaking

The `vrf-route-leaking.yml` topology contains two VRFs:

* VRF *red* containing Linux hosts h1 and h2
* VRF *blue* containing Linux hosts h3 and h4

Routes from *red* VRF are imported into *red* and *blue* VRF. Likewise, the routes from *blue* VRF are imported into both VRFs.

After starting the lab, all hosts (h1..h4) should be able to ping all other hosts.

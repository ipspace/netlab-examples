# VRF Lite with CE Routers Test Cases

This directory contains *netlab* topology files describing several simple VRF Lite test cases containing a set of CE routers attached to a pair of PE routers running VRF Lite.

The test cases can be used with all network devices supporting VRF configuration module and all virtualization providers supported by *netlab*:

* To change the router device type for **pe1**, use `-s nodes.pe1.device=xxx` CLI argument
* To change the router device type for **pe2**, use `-s nodes.pe2.device=xxx` CLI argument
* To change the virtualization provider, use `-p` CLI argument.

For example, to start the lab with a Cisco IOSv router and an Arista vEOS router, use:

```
netlab up -s nodes.pe1.device=iosv -s nodes.pe2.device=eos <topo-name>
```

To start the lab with Arista cEOS (using *containerlab*) use:

```
netlab up -p clab -s nodes.pe1.device=eos -s nodes.pe2.device=eos <topo-name>
```

## Isolated VRFs

The `multi-vrf.yml` topology contains two isolated VRFs:

* VRF *red* containing CE-routers **cr1** and **cr2** running OSPF with PE-routers
* VRF *blue* containing CE-router **cb1** and **cb2** running BGP with PE-routers

The link between PE-routers and **cr1** is multi-access link, the other PE-CE links are point-to-point links (Arista vEOS could not establish a VRF BGP session over a multi-access link).

After starting the lab, **cr1** should be able to ping **cr2** but not **cb1** or **cb1**.

## Inter-VRF Route Leaking

The `vrf-route-leaking.yml` topology contains the same devices and links as the *Isolated VRFs* topology, the only difference is the route leaking between *red* and *blue* VRFs:

* Routes from *red* VRF are imported into *red* and *blue* VRF.
* Likewise, the routes from *blue* VRF are imported into both VRFs.

After starting the lab, all CE-routers should be able to ping each other.

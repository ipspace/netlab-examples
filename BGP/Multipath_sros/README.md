# BGP Add Path use case using Nokia SR OS and SR Linux nodes
![plot](Multipath_sros.PNG)

This example is a variation on this [BGP Add Path example](../Multipath), using
a pair of SR OS nodes (RR and M) and a set of SR Linux devices instead.

# Prerequisites
* [NetSim PR](https://github.com/ipspace/netsim-tools/pull/57) to add SROS/SRLinux support
* License file for the SR OS vSR VMs

# Instructions
```
netsim up
```

# Deep dive
This example uses the Initial, [OSPF](https://netsim-tools.readthedocs.io/en/latest/module/ospf.html)
and [BGP](https://netsim-tools.readthedocs.io/en/latest/module/bgp.html) modules to
provision a topology consisting of 7 nodes, 6 of which represent a network peering with an external network.

The 6 internal nodes use a BGP Route Reflector (RR) for iBGP peering, and the use case
revolves around providing optimal paths for each node in this asymmetric case. Specifically,
node M could use multiple ECMP paths to reach external node Y - using BGP Add Path.

In terms of capabilities, Nokia SR OS supports BGP Add Path ([RFC7911](https://datatracker.ietf.org/doc/html/rfc7911))
but SR Linux does not. That is why nodes RR and M are implemented using SR OS, while the rest can use SRLinux.

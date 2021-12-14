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
provision a topology consisting of 7 nodes, 6 of which represent a network peering with an external network (Y).

The 6 internal nodes use a BGP Route Reflector (RR) for iBGP peering, and the use case
revolves around providing optimal paths for each node in this asymmetric case. Specifically,
node M could use multiple ECMP paths to reach external node Y - using BGP Add Path.

In terms of capabilities, Nokia SR OS supports BGP Add Path ([RFC7911](https://datatracker.ietf.org/doc/html/rfc7911))
but SR Linux does not. That is why nodes RR and M are implemented using SR OS, while the rest can use SRLinux.

## Base state without BGP Add Path
After commenting out the 'bgp-addpath.js' custom config template, the initial state is as follows:

Every node is fully connected to OSPF neighbors:
```
A:admin@rr# show router ospf neighbor

===============================================================================
Rtr Base OSPFv2 Instance 0 Neighbors
===============================================================================
Interface-Name                   Rtr Id          State      Pri  RetxQ   TTL
   Area-Id
-------------------------------------------------------------------------------
i1/1/c1                          10.0.0.3        Full       1    0       30
   0.0.0.0
i1/1/c2                          10.0.0.5        Full       1    0       30
   0.0.0.0
-------------------------------------------------------------------------------
No. of Neighbors: 2
===============================================================================
```

The Route Reflector (RR) receives the external prefix 10.42.42.0/24 from both C and D,
picking D because of the lower IGP cost from its perspective, 1 (via D) versus 17 via D(10.0.0.5) and then C(10.0.0.4):
```
A:admin@rr# show router bgp neighbor "10.0.0.4" received-routes | match 10.42.42.0 post-lines 2
*?    10.42.42.0/24                                      100         None
      10.0.0.4                                           None        17
      65100                                                          -

[/]
A:admin@rr# show router bgp neighbor "10.0.0.5" received-routes | match 10.42.42.0 post-lines 2
u*>?  10.42.42.0/24                                      100         None
      10.0.0.5                                           None        1
      65100                                                          -
```

It sends this single best route (via D) to M:
```
A:admin@rr# show router bgp neighbor "10.0.0.6" advertised-routes | match 10.42.42.0 post-lines 2
?     10.42.42.0/24                                      100         None
      10.0.0.5                                           None        1
      65100                                                          -
```

### Adding BGP Add Path
```
netlab config bgp-addpath.j2
```

This configures both RR and M to support BGP Add path extensions, and in addition
configures the RR to ignore the IGP cost difference (as the cost can be different from client perspective)

This causes the RR to use both routes:
```
A:admin@rr# show router bgp routes | match 10.42.42.0 post-lines 2
===============================================================================
BGP IPv4 Routes
===============================================================================
Flag  Network                                            LocalPref   MED
      Nexthop (Router)                                   Path-Id     IGP Cost
      As-Path                                                        Label
-------------------------------------------------------------------------------
...
u*>?  10.42.42.0/24                                      100         None
      10.0.0.4                                           None        17
      65100                                                          -
u*>?  10.42.42.0/24                                      100         None
      10.0.0.5                                           None        1
      65100                                                          -
```

and to announce both to M, assigning different path IDs (1 via C, 2 via D):
```
A:admin@rr# show router bgp neighbor "10.0.0.6" advertised-routes | match 10.42.42 post-lines 2
?     10.42.42.0/24                                      100         None
      10.0.0.5                                           2           1
      65100                                                          -
?     10.42.42.0/24                                      100         None
      10.0.0.4                                           1           17
      65100                                                          -
```

At client M, both routes become active:
```
A:admin@m# show router bgp routes | match 10.42.42.0 post-lines 2
u*>?  10.42.42.0/24                                      100         None
      10.0.0.4                                           1           1
      65100                                                          -
u*>?  10.42.42.0/24                                      100         None
      10.0.0.5                                           2           1
      65100                                                          -
```

allowing M to reach Y via ECMP routes, via C and D:
```
A:admin@m# show router route-table | match 10.42.42.0 post-lines 1
10.42.42.0/24                                 Remote  BGP       00h01m03s  170
       10.1.0.33                                                    1
10.42.42.0/24                                 Remote  BGP       00h01m03s  170
       10.1.0.37                                                    1
```

each having the same IGP cost (1)
```
A:admin@m# show router bgp routes | match 10.42.42.0 post-lines 2
u*>?  10.42.42.0/24                                      100         None
      10.0.0.4                                           1           1
      65100                                                          -
u*>?  10.42.42.0/24                                      100         None
      10.0.0.5                                           2           1
      65100                                                          -
```

# Discussion: A BGP Anycast alternative
In [this blog](https://srlinux-at-your-service.medium.com/do-it-yourself-automation-for-bgp-anycast-introducing-one-next-hop-to-rule-them-all-173e21237a1f) an alternative solution is suggested, using BGP Anycast nexthops.

Originally, the IGP topology used there was slightly different, using eBGP instead of OSPF.
This leads to the RR sending routes with full AS paths to its clients, instead of an (aggregated) IGP cost metric from OSPF.

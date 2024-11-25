# EVPN Designs: IBGP-over-EBGP

This directory contains the lab topology described in the [EVPN Designs:
IBGP-over-EBGP](https://blog.ipspace.net/2024/11/evpn-designs-ibgp-ebgp/) blog
post.

![](http://blog.ipspace.net/2024/04/evpn-design-fabric.png)

The switches run EBGP (IPv4 AF) on physical interfaces and IBGP (EVPN AF)
between lopback interfaces advertised via EBGP IPv4 AF.

![](https://blog.ipspace.net/2024/11/evpn-design-ibgp-over-ebgp-asn.png)

The `eos` and `frr` directories contain the device configurations for leaf-
and spine switches running Arista EOS or FRRouting.

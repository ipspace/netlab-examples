# EVPN Designs: EBGP-over-EBGP

This directory contains the lab topology described in the [EVPN Designs:
EBGP-over-EBGP](https://blog.ipspace.net/2024/10/evpn-designs-ebgp-ebgp/) blog
post. 

![](http://blog.ipspace.net/2024/04/evpn-design-fabric.png)

The switches run EBGP (IPv4 AF) on physical interfaces and EBGP (EVPN AF)
between lopback interfaces advertised via EBGP IPv4 AF.

![](https://blog.ipspace.net/2024/10/evpn-design-ebgp-over-ebgp.png)

The lab topology uses a custom EBGP ECMP configuration template that is provided
for Arista EOS and FRRouting and reports a warning if you're using another
device for the leaf switches.

If you need a similar template for another platform, please add the
configuration template to the `ebgp.ecmp` directory and submit a Pull Request.

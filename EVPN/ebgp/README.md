# EVPN Designs: EBGP Everywhere

This directory contains the lab topology described in the [EVPN Designs: EBGP Everywhere
](https://blog.ipspace.net/2024/10/evpn-designs-ebgp/) blog post. The spine switches are route reflectors
for the EVPN address family, the leaf switches are route-reflector clients.

![](http://blog.ipspace.net/2024/04/evpn-design-fabric.png)

The lab topology uses a custom EBGP ECMP configuration template that is provided for Arista EOS and FRRouting and reports a warning if you're using another device for the leaf switches.

If you need a similar template for another platform, please add the configuration template to the `ebgp.ecmp` directory and submit a Pull Request.

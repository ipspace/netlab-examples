This is a leaf-spine topology that uses Arista's iBGP over eBGP model of 
running EVPN. It utilizes a dual-stack throughout, and runs VXLAN with an
IPv6 header, and IPv4 packets are carried encapsulated by this IPv6 VXLAN
as well. 

We also have a dcedge node that runs in a different VRF and we leak routes
between the evpn vrf and the internet vrf. I should've added a firewall node
as well, but lacked the time.

The specific route maps and such may make this workable only with EOS for now.

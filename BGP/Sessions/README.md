# Testing BGP Sessions from Unknown Sources

This directory contains lab topologies used to test implementations of BGP session security features:

* `unknown-source-ip.yml` tests the device behavior when receiving a TCP SYN packet from an unknown IP address. The results are described in the _"[Will Network Devices Reject BGP Sessions from Unknown Sources?](https://blog.ipspace.net/2023/10/reject-unknown-bgp-session.html)"_ blog post.
* `gtsm.yml` tests the behavior of a BGP speaker configured with TTL session protection (GTSM) when receiving TCP packets with too-low TTL.

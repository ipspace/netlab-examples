# Small Site Multihoming

This directory contains the [netlab topology](topology.yml) and the router configurations for the [Small-Site Multihoming](https://blog.ipspace.net/kb/Internet/MH_SOHO/) article

![](https://blog.ipspace.net/kb/Internet/MH_SOHO/MultihomedSOHO_2.jpg)

The router configurations were collected for each section of the article:

* [gw-basic-config.cfg](gw-basic-config.cfg) for [Configuring Small Multi-Homed Site](https://blog.ipspace.net/kb/internet/mh_soho/20-config/)
* [gw-reliable-static-routes.cfg](gw-reliable-static-routes.cfg) for [Not-so-Very-Static Routes](https://blog.ipspace.net/kb/internet/mh_soho/30-not-so-static/)
* [gw-eem-applet.cfg](gw-eem-applet.cfg) for [Monitoring Reliable Static Routing](https://blog.ipspace.net/kb/internet/mh_soho/40-monitor/)
* [gw-dual-sla.cfg](gw-dual-sla.cfg) for the [End-to-End Connectivity Test](https://blog.ipspace.net/kb/internet/mh_soho/50-end-to-end-test/)

The directory also includes two netlab custom configuration templates you can use to shut down or reenable the link toward the customer on the PE routers running FRRouting or Cumulus Linux.

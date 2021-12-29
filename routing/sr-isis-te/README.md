# Example: ePipe service over SR-ISIS with Traffic Engineering and MACsec

Netsim-Tools release 1.0.6 introduces support for [custom plugins](https://github.com/ipspace/netsim-tools/blob/master/docs/plugins.md).
This example illustrates 3 of them:
* An MPLS-TE plugin to define custom MPLS paths
* An SDP ePipe plugin to build ePipe services
* A MACSEC plugin to configure security parameters

All plugins are relatively simple, by design; following the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy):
* Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features".
* Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.
* Design and build software, even operating systems, to be tried early, ideally within weeks. Don't hesitate to throw away the clumsy parts and rebuild them.
* Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after you've finished using them.

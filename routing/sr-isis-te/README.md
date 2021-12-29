# L2 example: ePipe service over SR-ISIS with Traffic Engineering and MACsec

See [original use case by Derek Cheung](https://medium.com/r/?url=https%3A%2F%2Fderekcheung.medium.com%2Fsegment-routing-b69f6ea2e3f5)

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

## Modeling extended L2 segments
This use case is different in that it models an extended L2 service: Host 1 and host 2 are both on the same subnet,
separated by an MPLS network topology that features a traffic-engineered ePipe service over SR-ISIS.

Netsim-Tools currently assumes 'atomic' links, i.e. different links are assigned different prefixes from a pool.
This example uses custom manual addressing; including these concepts in Netsim-Tools is FFS.

## MACsec: For Future Study / work in progress
Note that the MACsec association doesn't currently work in this setup: MACsec is designed for hop-by-hop security, and this multi-hop MPLS scenario requires more thought/knobs.

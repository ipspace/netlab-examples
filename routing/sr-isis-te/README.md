# L2 example: ePipe service over SR-ISIS with Traffic Engineering and MACsec

See [original use case by Derek Cheung](https://medium.com/r/?url=https%3A%2F%2Fderekcheung.medium.com%2Fsegment-routing-b69f6ea2e3f5)

This example uses three *netlab* [custom plugins](https://github.com/ipspace/netsim-tools/blob/master/docs/plugins.md):

* An SDP ePipe plugin to build ePipe services (both local and distributed)
* An MPLS-TE plugin to define custom MPLS paths (depends on SDP plugin)
* A MACsec plugin to configure security parameters

All plugins are relatively simple, by design; following the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy):
* Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features".
* Expect the output of every program to become the input to another, as yet unknown, program. Don't clutter output with extraneous information. Avoid stringently columnar or binary input formats. Don't insist on interactive input.
* Design and build software, even operating systems, to be tried early, ideally within weeks. Don't hesitate to throw away the clumsy parts and rebuild them.
* Use tools in preference to unskilled help to lighten a programming task, even if you have to detour to build the tools and expect to throw some of them out after you've finished using them.

## Modeling extended(stretched) L2 segments
This use case is different in that it models an extended L2 service: Host 1 and host 2 are both on the same subnet,
separated by an MPLS network topology that features a traffic-engineered ePipe service over SR-ISIS.

netlab currently assumes 'atomic' links, i.e. different links are assigned different prefixes from a pool.
This example uses custom manual addressing, selectively removing IP addresses from interfaces as needed.

## MACsec on 7x50
MACsec ([IEEE 802.1AE](https://1.ieee802.org/security/802-1ae/)) is designed to provide hop-by-hop security through encryption and replay protection.
Two (or more) peer nodes form a security association by exchanging EAPOL messages (MKA protocol), establishing encryption keys.

On 7x50, MACsec is supported on a select set of chassis types and MDAs (as of 21.10.R2):
* SR-1s/2s/7s/14s: ms8-100gb-sfpdd+2-100gb-qsfp28 and ms16-100gb-sfpdd+4-100gb-qsfp28
* SR-1e/2e/3e/7/12(e): me12-10/1gb-sfp+ (iom-e)
* SR-a4/a8: maxp10-10/1gb-msec-sfp+ (iom-a)
* IXR-6/10: imm36-100g-qsfp28 and imm48-sfp+2-qsfp28
* IXR-R4/R6: m6-10g-sfp++1-100g-qsfp28 and m10-10g-sfp+

The [vSIM installation guide](https://documentation.nokia.com/cgi-bin/dbaccessfilename.cgi/3HE17166AAADTQZZA01_V1_vSIM%20Installation%20and%20Setup%20Guide%2021.10.R1.pdf) lists the supported combinations
and the resource requirements for each option. Specifically, out of this list only SR-1s and IXR-R6 are supported
as 'integrated' single-VM devices (to minimize resource requirements)

A minimal single integrated VM configuration that supports MACsec is the following:
* Device: SR-1s (integrated CPM/DP)
* vCPUs: 2
* RAM: 6GB (due to 'xcm-1s' card)
* max NICs: 20 x 100G (ms16-100gb-sfpdd+4-100gb-qsfp28)

In Containerlab, this can be realized using a custom 'provider_type' line:
```
provider_type: "cpu=2 ram=6 max_nics=20 slot=A chassis=sr-1s card=xcm-1s xiom/x1=iom-s-3.0t mda/x1/1=ms16-100gb-sfpdd+4-100gb-qsfp28"
```
For your convenience, a PR to support this configuration natively as a 'sr-1s-macsec' profile has been submitted.

# SRLinux SR-MPLS example using SR-ISIS

Commemorating the [release of SR Linux 21.11.1](https://documentation.nokia.com/srlinux/SR_Linux_HTML_R21-11/Resources/pdf/Product_Overview_R21.11.pdf), now with SR-MPLS support (on 7250 IXR platforms), this repo presents an end-2-end topology featuring a BGP-free core.

X1 can ping X2:
```

A:x1# ping 10.0.0.6

Using network instance default
PING 10.0.0.6 (10.0.0.6) 56(84) bytes of data.
64 bytes from 10.0.0.6: icmp_seq=1 ttl=61 time=16.1 ms
64 bytes from 10.0.0.6: icmp_seq=2 ttl=61 time=16.7 ms

--- 10.0.0.6 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 16.118/16.423/16.729/0.331 ms
```

using an MPLS datapath via E1-{C1 or C2}-E2.

## Annotated configuration

```
--{ + running }--[ network-instance default protocols isis ]-
A:e1# info

    dynamic-label-block dynamic-srgb !!! Required but not currently used
    instance Gandalf {
        admin-state enable
        level-capability L2
        max-ecmp-paths 1 !!! SR-ISIS does not support ECMP in a production environment. The ISIS configuration of max-ecmp-paths must be 1. [398533]
        net [
            49.0001.0000.0000.0003.00
        ]
        segment-routing {
            mpls {
            }
        }
        interface ethernet-1/1.0 {
            circuit-type point-to-point
            passive false
            ipv4-unicast {
                admin-state enable
                enable-bfd false
            }
        }
        interface ethernet-1/2.0 {
            circuit-type point-to-point
            passive false
            ipv4-unicast {
                admin-state enable
                enable-bfd false
            }
        }
        interface ethernet-1/3.0 {
            admin-state disable !!! Disabled on external interface
        }
        interface system0.0 {
            passive true
            ipv4-unicast {
                admin-state enable
            }
            ipv6-unicast {
                admin-state disable
            }
            segment-routing {
                mpls {
                    ipv4-node-sid {
                        index 3 !!! References a label from the global static range
                    }
                }
            }
        }
    }
```

## Show commands

### Router E1 ISIS adjacencies:
```
--{ + running }--[  ]-
A:e1# show network-instance default protocols isis adjacency
---------------------------------------------------------------------------------------------------------------------------------------------
Network Instance: default
Instance        : Gandalf
+----------------+--------------------+-----------------+------------+--------------+-------+--------------------------+--------------------+
| Interface Name | Neighbor System Id | Adjacency Level | Ip Address | Ipv6 Address | State |     Last transition      | Remaining holdtime |
+================+====================+=================+============+==============+=======+==========================+====================+
| ethernet-1/1.0 | 0000.0000.0001     | L2              | 10.1.0.1   | ::           | up    | 2022-01-28T17:15:09.500Z | 27                 |
| ethernet-1/2.0 | 0000.0000.0002     | L2              | 10.1.0.5   | ::           | up    | 2022-01-28T17:15:09.400Z | 27                 |
+----------------+--------------------+-----------------+------------+--------------+-------+--------------------------+--------------------+
Adjacency Count: 2
```

### Router E1 ISIS database for C1:
```
--{ + running }--[  ]-A:e1# show network-instance default protocols isis database 2 lsp-id 0000.0000.0001.00-00 detail
---------------------------------------------------------
Network Instance: default
Instance        : Gandalf
---------------------------------------------------------
Level Number: 2
Lsp Id      : 0000.0000.0001.00-00
Sequence    : 0x4f, checksum:0x9fbe, Lifetime:1199
Attributes  : L1 L2
+-------+---------------------------+--------+----------+
| Index |            Tlv            | Metric | Sub tlvs |
+=======+===========================+========+==========+
| 1     | area-addresses['49.0001'] |        |          |
| 2     | hostname c1               |        |          |
| 3     | Protocol                  |        |          |
|       | Supported:['IPv6',        |        |          |
|       | 'IPv4']                   |        |          |
| 4     | IPv4 Interface Address:   |        |          |
|       | ['10.0.0.1', '10.1.0.1',  |        |          |
|       | '10.1.0.9']               |        |          |
| 5     | IPv6 Interface Address:   |        |          |
|       | []                        |        |          |
| 6     | IS extended neighbor:     | 10     | IP       |
|       | 0000.0000.0003.00         |        | address: |
|       |                           |        | 10.1.0.1 |
| 7     | IS extended neighbor:     | 10     | IP       |
|       | 0000.0000.0004.00         |        | address: |
|       |                           |        | 10.1.0.9 |
| 8     | IP Extended prefix:       | 0      |          |
|       | 10.0.0.1/32               |        |          |
| 9     | IP Extended prefix:       | 10     |          |
|       | 10.1.0.0/30               |        |          |
| 10    | IP Extended prefix:       | 10     |          |
|       | 10.1.0.8/30               |        |          |
+-------+---------------------------+--------+----------+
```

### Router E1 tunnel table with node SIDs
```
--{ + running }--[ network-instance default ]-

A:e1# show tunnel-table all
-------------------------------------------------------------------------------------------------------------------------------------------------
IPv4 tunnel table of network-instance "default"
-------------------------------------------------------------------------------------------------------------------------------------------------
+-------------+-------------+-------------+-----------+-----+--------+------------+--------------------------+-----------------+----------------+
| IPv4 Prefix | Encaps Type | Tunnel Type | Tunnel ID | FIB | Metric | Preference |       Last Update        | Next-hop (Type) |    Next-hop    |
+=============+=============+=============+===========+=====+========+============+==========================+=================+================+
| 10.0.0.1/32 | mpls        | sr-isis     | 500001    | Y   | 10     | 11         | 2022-01-28T17:15:18.254Z | 10.1.0.1 (mpls) | ethernet-1/1.0 |
| 10.0.0.2/32 | mpls        | sr-isis     | 500002    | Y   | 10     | 11         | 2022-01-28T17:15:22.277Z | 10.1.0.5 (mpls) | ethernet-1/2.0 |
| 10.0.0.4/32 | mpls        | sr-isis     | 500004    | Y   | 20     | 11         | 2022-01-28T17:15:18.255Z | 10.1.0.1 (mpls) | ethernet-1/1.0 |
+-------------+-------------+-------------+-----------+-----+--------+------------+--------------------------+-----------------+----------------+
-------------------------------------------------------------------------------------------------------------------------------------------------
3 SR-ISIS tunnels, 3 active, 0 inactive
```

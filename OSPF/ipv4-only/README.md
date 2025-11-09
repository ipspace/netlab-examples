# Deploy Only OSPFv2 in a Dual-Stack Lab

This simple lab topology deploys a dual-stack network (every interface has both an IPv4 and an IPv6 address), but limits OSPF configuration to OSPFv2, allowing you to practice configuring OSPFv3.

To kick the tires, set up a _netlab_ environment ([installation guide](https://netlab.tools/install/) or use [GitHub Codespaces](/2024/07/netlab-examples-codespaces/)

If you set up your own netlab environment, execute `netlab up https://github.com/ipspace/netlab-examples/blob/master/OSPF/ipv4-only/topology.yml` in an empty directory. If you didn't install Arista cEOS containers, add `-d frr` to the command.

In a GitHub Codespace:

* Install [Arista cEOS container image](https://blog.ipspace.net/2024/07/arista-eos-codespaces/)
* Change directory to `OSPF/ipv4-only`
* Execute **netlab up**, or **netlab up -d frr** to use FRRouting if you didn't install the Arista cEOS container image.

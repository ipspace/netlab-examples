## DMVPN lab topology
In this lab topology a situation is simulated where an IPsec interconnect to a 4G IoT provider is used to connect 4G enabled spoke routers to local hub routers. After running `netlab up` run `netlab config iosv.j2` to deploy the DMVPN configuration.

![DMVPN topology](dmvpn.png)

Some notes:
- The IoT provider / underlay network is simulated with static routes.
- An ACL prevents direct traffic between spokes over the 4G underlay, simulating the properties of a 4G network.
- In the lab a routed IPsec tunnel is used whereas a provider would typically use a policy based IPsec tunnel. 
- In the `lab 10.0.1.0/24` is part of the (imaginary) P2 proposal, `10.0.1.0/29` is used for the hub interconnects and as such is part of both the underrlay as well as the overlay network. 
- To counter recursive routing the spokes are configured with an specific route for the /29 subnet.
- IPsec encryption of the GRE tunnels can be added by adding the IPsec policy and transform set etc. as well as the `tunnel protection IPsec profile <ipsec profile>` statement on the tunnel interfaces, with the additional keyword `shared` added to the spoke tunnel interfaces.

# DHCP relaying

This directory contains *netlab* topology file for a simple DHCP relaying scenario.

![DHCP relaying topology](dhcp-relay.png)

After starting the lab, the *user* device should get DHCP-assigned IP address on its lab-facing interface.

## Changing Device Types

This topology can be used with Cisco IOSv, Arista EOSv, or Linux ISC DHCP relay. To test it with other devices, add custom configuration template to `dhcp-relay` directory.

The easiest way to change the device types is to edit the topology file. You could also use the **netlab up** [CLI arguments](https://netsim-tools.readthedocs.io/en/latest/netlab/up.html#usage) -- to change the DHCP relay device type, use `-s nodes.relay.device=xxx` CLI argument.

To use the ISC DHCP relay, you have to add `role: router` to the  **dhcp_server** group. See the [Linux VM](linux-vm.yml)  topology for more details.

## Using Linux as the DHCP Client

The default lab topology uses Cisco IOSv as the DHCP client and server. You can use a Linux VM or a Linux container as a DHCP client if you don't have access to Cisco IOSv.

To use a Ubuntu VM as a DHCP client, replace the `device: iosv` parameter in **dhcp_client** group in the lab topology with `device: linux`. The configuration scripts in the `dhcp-client` directory modify the *netplan* configuration files to use `systemd.networkd` DHCP client.

To use a Linux container, replace the `device: iosv` parameter in **dhcp_client** group in the lab topology with `device: linux`, add `provider: clab` to the group definition if needed[^LVO], and specify the client image with `clab.image: alpine` (the default _netlab_ Linux container image does not include a DHCP client).

See the [Linux VM](linux-vm.yml) and [Linux containers](linux-clab.yml) topologies for more details.

[^LVO]: Multi-provider topologies work only with *libvirt* as the primary provider.

## Using Linux as the DHCP Server

The default lab topology uses Cisco IOSv or CSR 1000v (IOS XE) as the DHCP server. You can replace them with a Linux VM or a Linux container running *dnsmasq*.

To use a Ubuntu VM as a DHCP server, replace the `device: iosv` parameter in **dhcp_server** group in the lab topology with `device: linux`. The configuration scripts in the `dhcp-server` directory were tested with a Ubuntu VM with dynamically installed *dnsmasq*.

To use a Linux container as a DHCP server, use the following definition for the **dhcp_server** group[^LVO]:

```
  dhcp_server:
    members: [ srv ]
    device: linux
    clab.image: strm/dnsmasq
    clab.config_templates:
      "dhcp-server/dnsmasq" : "/etc/dnsmasq.conf"
    provider: clab
```

See the [Linux VM](linux-vm.yml) and [Linux containers](linux-clab.yml) topologies for more details.

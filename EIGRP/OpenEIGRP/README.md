# Testing OpenEIGRP with netlab

This directory contains several lab topologies you can use to test OpenEIGRP containers with netlab. You can start the lab locally or in GitHub Codespaces.

## Using GitHub Codespaces

* Start a new GitHub Codespace

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ipspace/netlab-examples)

* Change directory to `EIGRP/OpenEIGRP`
* Execute `netlab up` to start the baseline lab (two OpenEIGRP/FRRouting containers).

You might be able to import a Cisco IOL container into the codespace and start the multi-vendor lab with `netlab up frr-iol.yml` (I did not test it)

## Local Tests

* Install netlab
* Clone this repository and follow the above instructions, or download the lab topology while starting the lab (replace `topology.yml` with the name of the lab topology you want to start)

```bash
netlab up https://github.com/ipspace/netlab-examples/blob/master/EIGRP/OpenEIGRP/topology.yml
```

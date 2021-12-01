'''
Custom plugin for BGP anycast scenario

Removes IBGP sessions from the members of the 'anycast' group
'''

import sys
from box import Box
from netsim.augment import topology
from netsim import common

def post_transform(topo: Box) -> None:
  for node in topo.nodes:
    if 'bgp' in node:
      if 'anycast' in node.bgp:
        node.bgp.advertise_loopback = False
        node.bgp.neighbors = [ n for n in node.bgp.neighbors if n.type != 'ibgp' ]

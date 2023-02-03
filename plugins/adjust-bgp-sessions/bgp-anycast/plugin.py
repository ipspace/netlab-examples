'''
Custom plugin for BGP anycast scenario

Removes IBGP sessions from the members of the 'anycast' group
'''

from box import Box
from netsim import api

def init(topo: Box) -> None:
  topo.defaults.bgp.attributes.node.anycast = { 'type': 'ipv4', 'use': 'prefix' }

def post_transform(topo: Box) -> None:
  for name,node in topo.nodes.items():
    if 'anycast' in node.get('bgp',{}):
      node.bgp.advertise_loopback = False
      node.bgp.neighbors = [ n for n in node.bgp.neighbors if n.type != 'ibgp' ]

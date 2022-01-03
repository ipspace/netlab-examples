'''
Custom plugin for BGP anycast scenario

Removes IBGP sessions from the members of the 'anycast' group
'''

import sys
from box import Box
from netsim.augment import topology
from netsim import common
from netsim import api

def init(topo: Box) -> None:
  topo.defaults.bgp.attributes.node.append('anycast')

def post_transform(topo: Box) -> None:
  config_name = api.get_config_name(globals())
  for node in topo.nodes:
    if 'anycast' in node.get('bgp',{}):
      node.bgp.advertise_loopback = False
      node.bgp.neighbors = [ n for n in node.bgp.neighbors if n.type != 'ibgp' ]
      api.node_config(node,config_name)
